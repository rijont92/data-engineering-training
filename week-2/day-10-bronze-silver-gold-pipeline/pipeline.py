import csv
import os
import datetime

# Part 1 - Bronze
def load_csv(file_path):

    rows = []

    with open(file_path, "r", newline="", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        reader.fieldnames = [
            field.strip()
            for field in reader.fieldnames
        ]

        for row in reader:
            rows.append(row)

    return rows

def ensure_output_folders():

    os.makedirs("data/silver", exist_ok=True)
    os.makedirs("data/gold", exist_ok=True)

def write_csv(file_path, rows, fieldnames):

    with open(file_path, "w", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(rows)


def load_orders():
    orders = load_csv("data/bronze/orders_raw.csv")
    print(f"Loaded raw orders: {len(orders)}")
    return orders


def load_customers():
    customers = load_csv("data/bronze/customers_raw.csv")
    print(f"Loaded raw customers: {len(customers)}")
    return customers


def load_products():
    products = load_csv("data/bronze/products_raw.csv")
    print(f"Loaded raw products: {len(products)}")
    return products



# Part 2 - Silver

def normalize_status(status):
    if not status:
        return "unknown"
    
    status = status.strip().lower()
    
    if status in ["completed","complete","done"]:
        return "completed"
    
    elif status in ["cancelled","canceled"]:
        return "cancelled"
    
    elif status == "pending":
        return "pending"
    
    else:
        return "unknown"
    
def normalize_channel(channel):
    if not channel:
        return "unknown"
    
    channel = channel.strip().lower()
    
    if channel in ["online","web","mobile"]:
        return "online"
    elif channel == "store":
        return "store"
    else:
        return "unknown"
    
def normalize_city(city):
    if not city or not city.strip():
        return "Unknown"

    city = city.strip().lower()

    city_mapping = {
        "prishtina": "Prishtina",
        "vushtrri": "Vushtrri"
    }

    return city_mapping.get(city, city.title())
    
def is_positive_integer(value):
    if not value:
        return False
    
    try:
        number = int(value)
        
        if number > 0:
            return True
        else:
            return False
            
    except (ValueError, TypeError):
        return False

def is_positive_number(value):
    if not value:
        return False

    try:
        number = float(value)

        if number > 0:
            return True
        else:
            return False

    except (ValueError, TypeError):
        return False

def build_lookup(rows, key_field):
    lookup = {}
    for row in rows:
        key = row[key_field]
        lookup[key] = row
    return lookup
    
def validate_order(order,customers_lookup,products_lookup,seen_order_ids):
    
    order_id = order["order_id"]

    if not order_id:
        return False, "missing_order_id"

    if order_id in seen_order_ids:
        return False, "duplicate_order_id"

    seen_order_ids.add(order_id)
    
    
    customer_id = order.get("customer_id")
    
    if not customer_id or customer_id not in customers_lookup:
        return False,"invalid_customer_id"
    
    product_id = order.get("product_id")
    
    if not product_id or product_id not in products_lookup:
        return False,"invalid_product_id"
    
    if not order.get("order_date"):
        return False,"missing_order_date"
    
    quantity = order.get("quantity")
    
    if not quantity:
        return False,"missing_quantity"
    
    if not is_positive_integer(quantity):
        if quantity.startswith("-"):
            return False,"negative_quantity"
        return False,"invalid_quantity"
    
    status = normalize_status(order.get("status"))
    
    
    if not order.get("status"):
        return False,"missing_status"
    
    if status == "unknown":
        return False,"invalid_status"
    
    channel = normalize_channel(order.get("channel"))
    if channel not in ["online","store","unknown"]:
        return False,"invalid_channel"
    
    return True,None

def calculate_total_amount(order):
    quantity = int(order["quantity"])
    price = float(order["price"])
    
    return round(quantity * price,2)
    
def enrich_order(order,customer_lookup,products_lookup):
    customer = customer_lookup[order["customer_id"]]
    product = products_lookup[order["product_id"]]
    
    enriched_order = {
        "order_id": order["order_id"],
        "customer_id": order["customer_id"],
        "customer_name": customer["customer_name"],
        "city": normalize_city(customer["city"]),
        "product_id": order["product_id"],
        "product_name": product["product_name"],
        "category": product["category"] if product["category"] else "Unknown",
        "quantity": order["quantity"],
        "price": product["price"],
        "total_amount": calculate_total_amount(
            {
                "quantity": order["quantity"],
                "price": product["price"]
            }
        ),
        "status": normalize_status(
            order["status"]
        ),
        "channel": normalize_channel(
            order["channel"]
        ),
        "order_date": order["order_date"]
    }
    return enriched_order

def clean_customers(raw_customers):

    cleaned = []
    seen = set()

    for customer in raw_customers:

        customer_id = customer["customer_id"]

        if customer_id in seen:
            continue

        seen.add(customer_id)

        cleaned.append({
            "customer_id": customer_id,
            "customer_name": customer["customer_name"].strip(),
            "city": normalize_city(customer["city"])
        })

    return cleaned

def clean_products(raw_products):

    cleaned = []

    for product in raw_products:

        if not is_positive_number(product["price"]):
            continue

        category = product["category"].strip()

        if not category:
            category = "Unknown"

        cleaned.append({
            "product_id": product["product_id"],
            "product_name": product["product_name"].strip(),
            "category": category,
            "price": float(product["price"])
        })

    return cleaned

def create_silver_orders(raw_orders, customers_lookup, products_lookup):

    clean_orders = []
    invalid_orders = []

    seen_order_ids = set()


    for order in raw_orders:

        is_valid, reason = validate_order(
            order,
            customers_lookup,
            products_lookup,
            seen_order_ids
        )


        if is_valid:

            clean_orders.append(
                enrich_order(
                    order,
                    customers_lookup,
                    products_lookup
                )
            )

        else:

            invalid_orders.append({

                "order_id": order["order_id"],
                "customer_id": order["customer_id"],
                "product_id": order["product_id"],
                "order_date": order["order_date"],
                "quantity": order["quantity"],
                "status": order["status"],
                "channel": order["channel"],
                "reason": reason

            })


    return clean_orders, invalid_orders


# Part 3 - Gold

def count_by_field(rows, field_name):
    counts = {}

    for row in rows:
        value = row[field_name]
        counts[value] = counts.get(value, 0) + 1

    return counts


def create_revenue_by_category(clean_orders):
    report = {}
    
    for order in clean_orders:
        if order["status"] != "completed":
            continue

        category = order["category"]

        if category not in report:
            report[category] = {
                "category": category,
                "completed_revenue": 0,
                "total_completed_orders": 0
            }

        report[category]["completed_revenue"] += order["total_amount"]
        report[category]["total_completed_orders"] += 1

    return sorted(report.values(),key=lambda row: row["completed_revenue"],reverse=True)


def create_revenue_by_city(clean_orders):

    report = {}

    for order in clean_orders:

        if order["status"] != "completed":
            continue

        city = order["city"]

        if city not in report:
            report[city] = {
                "city": city,
                "completed_revenue": 0,
                "total_completed_orders": 0
            }

        report[city]["completed_revenue"] += order["total_amount"]
        report[city]["total_completed_orders"] += 1

    return sorted(report.values(),key=lambda row: row["completed_revenue"],reverse=True)


def create_revenue_by_customer(clean_orders):

    report = {}

    for order in clean_orders:

        if order["status"] != "completed":
            continue

        customer = order["customer_name"]

        if customer not in report:
            report[customer] = {
                "customer_name": customer,
                "city": order["city"],
                "completed_revenue": 0,
                "total_completed_orders": 0
            }

        report[customer]["completed_revenue"] += order["total_amount"]
        report[customer]["total_completed_orders"] += 1

    return sorted(report.values(),key=lambda row: row["completed_revenue"],reverse=True)


def create_top_products(clean_orders):

    report = {}

    for order in clean_orders:

        if order["status"] != "completed":
            continue

        product = order["product_name"]

        if product not in report:
            report[product] = {
                "product_name": product,
                "category": order["category"],
                "total_quantity_sold": 0,
                "completed_revenue": 0
            }

        report[product]["total_quantity_sold"] += int(order["quantity"])
        report[product]["completed_revenue"] += order["total_amount"]

    return sorted(report.values(),key=lambda row: row["completed_revenue"],reverse=True)


def create_executive_summary(raw_orders,clean_orders,invalid_orders,revenue_by_category,revenue_by_city,revenue_by_customer,top_products):
    
    total_raw_orders = len(raw_orders)
    valid_silver_orders = len(clean_orders)
    invalid_orders_count = len(invalid_orders)

    status_counts = count_by_field(clean_orders, "status")

    completed_orders = status_counts.get("completed", 0)
    pending_orders = status_counts.get("pending", 0)
    cancelled_orders = status_counts.get("cancelled", 0)

    completed_revenue = 0

    for order in clean_orders:
        if order["status"] == "completed":
            completed_revenue += order["total_amount"]

    top_category = "N/A"
    if revenue_by_category:
        top_category = revenue_by_category[0]["category"]

    top_city = "N/A"
    if revenue_by_city:
        top_city = revenue_by_city[0]["city"]

    top_customer = "N/A"
    if revenue_by_customer:
        top_customer = revenue_by_customer[0]["customer_name"]

    top_product = "N/A"
    if top_products:
        top_product = top_products[0]["product_name"]

    reason_counts = count_by_field(invalid_orders, "reason")

    most_common_invalid_reason = "N/A"

    if reason_counts:
        most_common_invalid_reason = max(
            reason_counts,
            key=reason_counts.get
        )

    with open(
        "data/gold/executive_summary.txt",
        "w",
        encoding="utf-8"
    ) as file:

        file.write("Executive Summary - Day 10 Pipeline\n\n")

        file.write(f"Total raw orders: {total_raw_orders}\n")
        file.write(f"Valid silver orders: {valid_silver_orders}\n")
        file.write(f"Invalid orders: {invalid_orders_count}\n")
        file.write(f"Completed orders: {completed_orders}\n")
        file.write(f"Pending orders: {pending_orders}\n")
        file.write(f"Cancelled orders: {cancelled_orders}\n")
        file.write(f"Completed revenue: {completed_revenue:.2f}\n")
        file.write(f"Top category: {top_category}\n")
        file.write(f"Top city: {top_city}\n")
        file.write(f"Top customer: {top_customer}\n")
        file.write(f"Top product: {top_product}\n")
        file.write(f"Most common invalid reason: {most_common_invalid_reason}\n")
        file.write(
            "Business recommendation: Focus on the highest revenue category and reduce invalid orders by improving data validation and data quality before loading into the Silver layer.\n"
        )



def sum_by_group(rows, group_field, amount_field):

    result = {}

    for row in rows:

        group = row[group_field]

        amount = float(row[amount_field])

        if group not in result:
            result[group] = 0

        result[group] += amount

    return result


def create_data_quality_report(raw_orders, clean_orders, invalid_orders, raw_customers, raw_products):
    reason_counts = {}
    for order in invalid_orders:
        reason = order["reason"]
        reason_counts[reason] = reason_counts.get(reason, 0) + 1

    duplicate_orders = reason_counts.get("duplicate_order_id", 0)
    missing_dates = reason_counts.get("missing_order_date", 0)
    
    invalid_quantities = (
        reason_counts.get("missing_quantity", 0) +
        reason_counts.get("negative_quantity", 0) +
        reason_counts.get("invalid_quantity", 0)
    )
    
    invalid_statuses = (
        reason_counts.get("missing_status", 0) +
        reason_counts.get("invalid_status", 0)
    )
    
    invalid_products = reason_counts.get("invalid_product_id", 0)
    invalid_customers = reason_counts.get("invalid_customer_id", 0)
    
    # Check invalid product prices in raw products
    invalid_prices_count = 0
    for p in raw_products:
        price_val = p.get("price", "").strip()
        if not is_positive_number(price_val):
            invalid_prices_count += 1
            
    # Check missing cities in raw customers
    missing_cities_count = 0
    for c in raw_customers:
        city_val = c.get("city", "").strip()
        if not city_val:
            missing_cities_count += 1
            
    raw_equals_silver_plus_invalid = "YES" if len(raw_orders) == len(clean_orders) + len(invalid_orders) else "NO"
    
    with open("data_quality_report.txt", "w", encoding="utf-8") as file:
        file.write("Validation Checks\n")
        file.write(f"Raw orders count: {len(raw_orders)}\n")
        file.write(f"Silver clean orders count: {len(clean_orders)}\n")
        file.write(f"Invalid orders count: {len(invalid_orders)}\n")
        file.write(f"Raw = Silver + Invalid: {raw_equals_silver_plus_invalid}\n")
        file.write(f"Customer IDs checked: {len(raw_customers)}\n")
        file.write(f"Product IDs checked: {len(raw_products)}\n")
        file.write(f"Duplicate order IDs found: {duplicate_orders}\n")
        file.write(f"Missing dates found: {missing_dates}\n")
        file.write(f"Invalid quantities found: {invalid_quantities}\n")
        file.write(f"Invalid statuses found: {invalid_statuses}\n")
        file.write(f"Invalid products found: {invalid_products}\n")
        file.write(f"Invalid customers found: {invalid_customers}\n")
        file.write(f"Invalid product prices found: {invalid_prices_count}\n")
        file.write(f"Missing customer cities found: {missing_cities_count}\n")
        file.write("Invalid records by reason:\n")
        for reason, count in sorted(reason_counts.items()):
            file.write(f"- {reason}: {count}\n")


def log_step(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] {message}"
    print(log_line)
    with open("pipeline_log.txt", "a", encoding="utf-8") as f:
        f.write(log_line + "\n")


def create_revenue_by_channel(clean_orders):
    report = {}
    for order in clean_orders:
        if order["status"] != "completed":
            continue
        channel = order["channel"]
        if channel not in report:
            report[channel] = {
                "channel": channel,
                "completed_revenue": 0.0,
                "total_completed_orders": 0
            }
        report[channel]["completed_revenue"] += order["total_amount"]
        report[channel]["total_completed_orders"] += 1
        
    for item in report.values():
        item["completed_revenue"] = round(item["completed_revenue"], 2)
        
    return sorted(report.values(), key=lambda x: x["completed_revenue"], reverse=True)


def create_invalid_reasons_summary(invalid_orders):
    counts = count_by_field(invalid_orders, "reason")
    rows = []
    for reason, count in counts.items():
        rows.append({
            "reason": reason,
            "count": count
        })
    return sorted(rows, key=lambda x: x["count"], reverse=True)


def detect_unsold_products(clean_products, clean_orders):
    sold_product_ids = set()
    for order in clean_orders:
        if order["status"] == "completed":
            sold_product_ids.add(order["product_id"])
            
    unsold = []
    for p in clean_products:
        if p["product_id"] not in sold_product_ids:
            unsold.append({
                "product_id": p["product_id"],
                "product_name": p["product_name"],
                "category": p["category"],
                "price": p["price"]
            })
    return unsold


def detect_customers_without_orders(clean_customers, clean_orders):
    customers_with_orders = set(order["customer_id"] for order in clean_orders)
    inactive = []
    for c in clean_customers:
        if c["customer_id"] not in customers_with_orders:
            inactive.append({
                "customer_id": c["customer_id"],
                "customer_name": c["customer_name"],
                "city": c["city"]
            })
    return inactive


def create_dashboard_data(clean_orders, invalid_orders, raw_orders, revenue_by_category, revenue_by_city, revenue_by_customer, top_products):
    total_raw = len(raw_orders)
    valid_silver = len(clean_orders)
    invalid_count = len(invalid_orders)
    
    completed_revenue = 0.0
    completed_orders = 0
    for order in clean_orders:
        if order["status"] == "completed":
            completed_revenue += order["total_amount"]
            completed_orders += 1
            
    top_cat = revenue_by_category[0]["category"] if revenue_by_category else "N/A"
    top_ct = revenue_by_city[0]["city"] if revenue_by_city else "N/A"
    top_cust = revenue_by_customer[0]["customer_name"] if revenue_by_customer else "N/A"
    top_prod = top_products[0]["product_name"] if top_products else "N/A"
    
    row = {
        "total_raw_orders": total_raw,
        "valid_silver_orders": valid_silver,
        "invalid_orders": invalid_count,
        "completed_revenue": round(completed_revenue, 2),
        "total_completed_orders": completed_orders,
        "top_category": top_cat,
        "top_city": top_ct,
        "top_customer": top_cust,
        "top_product": top_prod
    }
    
    return [row]


def main():
    ensure_output_folders()
    
    # Reset log file with the header
    with open("pipeline_log.txt", "w", encoding="utf-8") as f:
        f.write("Pipeline Log - Day 10\n")
    
    # Step 1: Load Bronze files
    orders = load_orders()
    customers = load_customers()
    products = load_products()
    log_step("Step 1: Loaded Bronze files.")

    # Step 2: Clean customers
    clean_customers_data = clean_customers(customers)
    log_step("Step 2: Cleaned customers.")

    # Step 3: Clean products
    clean_products_data = clean_products(products)
    log_step("Step 3: Cleaned products.")

    # Create lookups
    customers_lookup = build_lookup(
        clean_customers_data,
        "customer_id"
    )
    products_lookup = build_lookup(
        clean_products_data,
        "product_id"
    )

    # Step 4: Validate orders
    clean_orders, invalid_orders = create_silver_orders(
        orders,
        customers_lookup,
        products_lookup
    )
    log_step("Step 4: Validated orders.")
    log_step("Step 5: Created Silver clean orders.")
    log_step("Step 6: Created invalid orders file.")

    # Write Silver files
    write_csv(
        "data/silver/customers_clean.csv",
        clean_customers_data,
        ["customer_id", "customer_name", "city"]
    )
    write_csv(
        "data/silver/products_clean.csv",
        clean_products_data,
        ["product_id", "product_name", "category", "price"]
    )
    write_csv(
        "data/silver/orders_clean.csv",
        clean_orders,
        [
            "order_id",
            "customer_id",
            "customer_name",
            "city",
            "product_id",
            "product_name",
            "category",
            "quantity",
            "price",
            "total_amount",
            "status",
            "channel",
            "order_date"
        ]
    )
    write_csv(
        "data/silver/invalid_orders.csv",
        invalid_orders,
        [
            "order_id",
            "customer_id",
            "product_id",
            "order_date",
            "quantity",
            "status",
            "channel",
            "reason"
        ]
    )

    # Step 7: Create Gold revenue reports
    revenue_by_category = create_revenue_by_category(clean_orders)
    revenue_by_city = create_revenue_by_city(clean_orders)
    revenue_by_customer = create_revenue_by_customer(clean_orders)
    top_products = create_top_products(clean_orders)
    
    # Bonus Gold reports
    revenue_by_channel = create_revenue_by_channel(clean_orders)
    invalid_reasons_summary = create_invalid_reasons_summary(invalid_orders)
    unsold_products = detect_unsold_products(clean_products_data, clean_orders)
    inactive_customers = detect_customers_without_orders(clean_customers_data, clean_orders)
    dashboard_data = create_dashboard_data(
        clean_orders, invalid_orders, orders,
        revenue_by_category, revenue_by_city, revenue_by_customer, top_products
    )

    # Write Gold files
    write_csv(
        "data/gold/revenue_by_category.csv",
        revenue_by_category,
        ["category", "completed_revenue", "total_completed_orders"]
    )
    write_csv(
        "data/gold/revenue_by_city.csv",
        revenue_by_city,
        ["city", "completed_revenue", "total_completed_orders"]
    )
    write_csv(
        "data/gold/revenue_by_customer.csv",
        revenue_by_customer,
        ["customer_name", "city", "completed_revenue", "total_completed_orders"]
    )
    write_csv(
        "data/gold/top_products.csv",
        top_products,
        ["product_name", "category", "total_quantity_sold", "completed_revenue"]
    )
    write_csv(
        "data/gold/revenue_by_channel.csv",
        revenue_by_channel,
        ["channel", "completed_revenue", "total_completed_orders"]
    )
    write_csv(
        "data/gold/invalid_reasons_summary.csv",
        invalid_reasons_summary,
        ["reason", "count"]
    )
    write_csv(
        "data/gold/unsold_products.csv",
        unsold_products,
        ["product_id", "product_name", "category", "price"]
    )
    write_csv(
        "data/gold/inactive_customers.csv",
        inactive_customers,
        ["customer_id", "customer_name", "city"]
    )
    write_csv(
        "data/gold/dashboard_data.csv",
        dashboard_data,
        [
            "total_raw_orders",
            "valid_silver_orders",
            "invalid_orders",
            "completed_revenue",
            "total_completed_orders",
            "top_category",
            "top_city",
            "top_customer",
            "top_product"
        ]
    )
    log_step("Step 7: Created Gold revenue reports.")

    # Step 8: Created executive summary
    create_executive_summary(
        orders,
        clean_orders,
        invalid_orders,
        revenue_by_category,
        revenue_by_city,
        revenue_by_customer,
        top_products
    )
    
    # Create Data Quality Report
    create_data_quality_report(orders, clean_orders, invalid_orders, customers, products)
    
    log_step("Step 8: Created executive summary.")
    log_step("Pipeline completed successfully.")


if __name__ == "__main__":
    main()