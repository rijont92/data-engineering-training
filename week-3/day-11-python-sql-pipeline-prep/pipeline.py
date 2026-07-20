import csv
import os


def load_csv(filepath):    
    """Load a CSV file and return its rows as a list of dictionaries."""
    with open(filepath,"r",newline="",encoding="utf-8") as file:
        return list(csv.DictReader(file))

def write_csv(filepath, data):
    """Write a list of dictionaries to a CSV file, creating parent folders if needed."""
    if not data:
        return
    
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    with open(filepath, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


            
def load_orders():
    """Load raw order records from the Bronze layer."""
    orders = load_csv("data/bronze/orders_raw.csv")
    print(f"Loaded raw orders: {len(orders)}")
    return orders


def load_customers():
    """Load raw customer profiles from the Bronze layer."""
    customers = load_csv("data/bronze/customers_raw.csv")
    print(f"Loaded raw customers: {len(customers)}")
    return customers


def load_products():
    """Load raw product catalog details from the Bronze layer."""
    products = load_csv("data/bronze/products_raw.csv")
    print(f"Loaded raw products: {len(products)}")
    return products

# Normalise status,city,channel

def normalize_status(status):
    """Standardize order status values to: completed, pending, cancelled, or unknown."""
    if not status:
        return "unknown"
    
    status = status.strip().lower()
    
    if status in ["completed","done"]:
        return "completed"
    elif status == "pending":
        return "pending"
    elif status in ["cancelled","canceled"]:
        return "cancelled"
    else:
        return "unknown"

def normalize_city(city):
    """Standardize city names, mapping common variations to standard capitalization."""
    if not city:
        return "Unknown"
    city = city.strip().lower()
    city_mapping = {
        "vushtrri":"Vushtrri",
        "prishtina":"Prishtina",
        "mitrovica":"Mitrovica",
        "peja":"Peja",
        "prizren":"Prizren",
        "ferizaj":"Ferizaj",
        "gjilan":"Gjilan"
    }
    return city_mapping.get(city, city.title())
    

def normalize_channel(channel):
    """Standardize sales channel values to standard lowercase options."""
    if not channel:
        return "unknown"

    channel = channel.strip().lower()

    if channel == "online":
        return "online"
    elif channel == "store":
        return "store"
    elif channel == "web":
        return "web"
    elif channel == "bank":
        return "bank"
    else:
        return "unknown"
    

# Validation


def is_positive_integer(value):
    """Check if a string or number is a valid positive integer greater than zero."""
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



def build_lookup(rows, key_field):
    """Build a dictionary lookup mapping key_field to row dictionaries for quick O(1) joins."""
    lookup = {}
    for row in rows:
        key = row[key_field]
        lookup[key] = row
    return lookup



def validate_order(order, customers, products, order_ids):
    """Validate an order record for integrity, completeness, and matching references."""
    reasons = []

    if order["order_id"] in order_ids:
        reasons.append("Duplicate order_id")

    if not is_positive_integer(order["quantity"]):
        reasons.append("Invalid quantity")

    
    normalized_status = normalize_status(order["status"])

    if normalized_status == "unknown":
        reasons.append("Invalid status")

    if not order["order_date"]:
        reasons.append("Missing order_date")

    if order["customer_id"] not in customers:
        reasons.append("Invalid customer_id")

    if order["product_id"] not in products:
        reasons.append("Invalid product_id")

    return reasons


def get_customer(customer_id, customers):
    """
    Lookup customer details using customer_id
    """
    return customers.get(customer_id)


def get_product(product_id, products):
    """
    Lookup product details using product_id
    """
    return products.get(product_id)


def create_silver_orders(orders, customers, products):
    """Clean, join, and validate raw orders, splitting them into clean and invalid lists."""
    clean_orders = []
    invalid_orders = []

    order_ids = set()

    for order in orders:
        reasons = validate_order(
            order,
            customers,
            products,
            order_ids
        )

        order_ids.add(order["order_id"])

        if reasons:
            order["invalid_reason"] = ", ".join(reasons)
            invalid_orders.append(order)
            continue


        customer = get_customer(
        order["customer_id"],
        customers
        )

        product = get_product(
        order["product_id"],
        products
        )
        

        clean_orders.append({
            "order_id": order["order_id"],
            "customer_id": order["customer_id"],
            "customer_name": customer["customer_name"],
            "city": normalize_city(customer["city"]),
            "segment": customer["segment"],
            "product_id" : order["product_id"],
            "product_name": product["product_name"],
            "category": product["category"],
            "quantity": int(order["quantity"]),
            "price": float(product["price"]),
            "status": normalize_status(order["status"]),
            "order_date": order["order_date"],
            "channel": normalize_channel(order["channel"]),
            "total_amount": int(order["quantity"]) * float(product["price"])
        })

    return clean_orders, invalid_orders
    
        
def create_gold_reports(clean_orders):
    """Generate business-level aggregate reports and summaries from clean silver data."""
    completed = [
        order for order in clean_orders
        if order["status"] == "completed"
    ]


    city_report = {}
        
    
    for order in completed:
        city = order["city"]
        city_report[city] = city_report.get(city,0) + order["total_amount"]

    write_csv(
      "data/gold/revenue_by_city.csv",
    [
        {"city": k, "revenue": v}
        for k,v in city_report.items()
    ]
)
        
    category_report = {}

    for order in completed:
        category = order["category"]
        category_report[category] = category_report.get(category,0) + order["total_amount"]


    write_csv(
        "data/gold/revenue_by_category.csv",
        [
            {"category": k, "revenue": v}
            for k,v in category_report.items()
        ]
    )

    customers = {}

    for order in completed:
        name = order["customer_name"]

        customers[name] = customers.get(name,0) + order["total_amount"]
    top = sorted(
        customers.items(),
        key=lambda x:x[1],
        reverse=True
    )

    write_csv(
        "data/gold/top_customers.csv",
        [
            {
                "customer_name": name,
                "revenue": revenue
            }
            for name,revenue in top[:5]
        ]
    )

    os.makedirs("data/gold", exist_ok=True)
    with open(
        "data/gold/executive_summary.txt",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            f"""
            Executive Summary
            Completed Orders: {len(completed)}
            Total Revenue: {sum(o['total_amount'] for o in completed)}
            """
        )



def main():
    """Execute the full ELT/ETL pipeline from raw bronze data to validated gold reports."""
    orders = load_orders()
    customers_list = load_customers()
    products_list = load_products()
    customers = build_lookup(customers_list, "customer_id")
    products = build_lookup(products_list, "product_id")
    clean, invalid = create_silver_orders(
        orders,
        customers,
        products
    )
    write_csv(
        "data/silver/orders_clean.csv",
        clean
    )
    write_csv(
        "data/silver/invalid_orders.csv",
        invalid
    )

    create_gold_reports(clean)

    print("Pipeline completed successfully!")
if __name__ == "__main__":
    main()