from order_data import orders


def print_raw_count(records):
    print("Raw records:", len(records))


def print_first_three_records(records):
    print("\nFirst three raw records:")
    for order in records[:3]:
        print(f"  Order ID: {order['order_id']}")
        print(f"  Customer: {order['customer_name']}")
        print(f"  City: {order['city']}")
        print(f"  Product: {order['product']}")
        print(f"  Category: {order['category']}")
        print(f"  Quantity: {order['quantity']}")
        print(f"  Price: {order['price']}")
        print(f"  Status: {order['status']}")
        print(f"  Channel: {order['channel']}")
        print(f"  Date: {order['order_date']}")
        print()


def print_unique_raw_values(records):
    statuses = []
    cities = []
    categories = []
    channels = []

    for order in records:
        if order["status"] not in statuses:
            statuses.append(order["status"])
        if order["city"] not in cities:
            cities.append(order["city"])
        if order["category"] not in categories:
            categories.append(order["category"])
        if order["channel"] not in channels:
            channels.append(order["channel"])

    print("\nUnique raw values before cleaning:")

    print("Statuses:")
    for status in sorted(statuses):
        print(f"  - {status}")

    print("\nCities:")
    for city in sorted(cities):
        print(f"  - {city}")

    print("\nCategories:")
    for category in sorted(categories):
        print(f"  - {category}")

    print("\nChannels:")
    for channel in sorted(channels):
        print(f"  - {channel}")


def validate_order(order):
    reasons = []

    if order["customer_name"].strip() == "":
        reasons.append("Missing customer name")

    if order["quantity"] <= 0:
        reasons.append("Quantity must be greater than 0")

    if order["price"] <= 0:
        reasons.append("Price must be greater than 0")

    return reasons


def split_valid_and_invalid_orders(records):
    valid_orders = []
    invalid_orders = []
    for order in records:
        validation_errors = validate_order(order)
        if validation_errors:
            invalid_order = order.copy()
            invalid_order["reasons"] = validation_errors
            invalid_orders.append(invalid_order)
        else:
            valid_orders.append(order)
    return valid_orders, invalid_orders


def write_invalid_records(invalid_orders):
    with open("output/invalid_records.txt", "w", encoding="utf-8") as file:
        file.write("INVALID RECORDS REPORT\n")
        file.write("=" * 50 + "\n\n")

        for order in invalid_orders:
            file.write(f"Order ID: {order['order_id']}\n")
            file.write(f"Customer: {order['customer_name']}\n")
            file.write("Reasons:\n")
            for reason in order["reasons"]:
                file.write(f"  - {reason}\n")
            file.write("\n")


def write_validation_report(raw_records, valid_orders, invalid_orders, cleaned_valid_orders=None):
    raw_statuses = sorted(set(o["status"] for o in raw_records))
    raw_cities = sorted(set(o["city"] for o in raw_records))
    raw_categories = sorted(set(o["category"] for o in raw_records))
    raw_channels = sorted(set(o["channel"] for o in raw_records))

    with open("output/validation_report.txt", "w", encoding="utf-8") as file:
        file.write("DATA VALIDATION REPORT\n")
        file.write("=" * 50 + "\n\n")
        file.write(f"Raw records: {len(raw_records)}\n")
        file.write(f"Valid records: {len(valid_orders)}\n")
        file.write(f"Invalid records: {len(invalid_orders)}\n\n")

        file.write("Unique raw values before cleaning:\n")
        file.write(f"  Statuses:   {', '.join(raw_statuses)}\n")
        file.write(f"  Cities:     {', '.join(raw_cities)}\n")
        file.write(f"  Categories: {', '.join(raw_categories)}\n")
        file.write(f"  Channels:   {', '.join(raw_channels)}\n\n")

        if cleaned_valid_orders:
            clean_statuses = sorted(set(o["status"] for o in cleaned_valid_orders))
            clean_cities = sorted(set(o["city"] for o in cleaned_valid_orders))
            clean_categories = sorted(set(o["category"] for o in cleaned_valid_orders))
            clean_channels = sorted(set(o["channel"] for o in cleaned_valid_orders))

            file.write("Unique values after cleaning (valid records only):\n")
            file.write(f"  Statuses:   {', '.join(clean_statuses)}\n")
            file.write(f"  Cities:     {', '.join(clean_cities)}\n")
            file.write(f"  Categories: {', '.join(clean_categories)}\n")
            file.write(f"  Channels:   {', '.join(clean_channels)}\n\n")

        file.write("Invalid record details:\n")
        file.write("-" * 50 + "\n")

        for order in invalid_orders:
            file.write(f"Order ID {order['order_id']}: ")
            file.write(", ".join(order["reasons"]))
            file.write("\n")


def normalize_status(status):
    s = status.strip().lower()
    if s in ["completed", "complete"]:
        return "completed"
    return s


def normalize_city(city):
    c = city.strip()
    if c.lower() in ["prishtine", "prishtina"]:
        return "Prishtina"
    return c.title()


def normalize_category(category):
    return category.strip().title()


def normalize_channel(channel):
    return channel.strip().lower()


def calculate_total_amount(order):
    return order["quantity"] * order["price"]


def clean_order(order):
    cleaned = order.copy()
    cleaned["status"] = normalize_status(order["status"])
    cleaned["city"] = normalize_city(order["city"])
    cleaned["category"] = normalize_category(order["category"])
    cleaned["channel"] = normalize_channel(order["channel"])
    cleaned["total_amount"] = calculate_total_amount(order)
    return cleaned


def get_completed_orders(clean_orders):
    return [order for order in clean_orders if order["status"] == "completed"]


def calculate_completed_revenue(clean_orders):
    completed = get_completed_orders(clean_orders)
    return sum(order["total_amount"] for order in completed)


def count_by_field(records, field_name):
    summary = {}
    for r in records:
        val = r.get(field_name)
        summary[val] = summary.get(val, 0) + 1
    return summary


def sum_revenue_by_field(records, field_name):
    summary = {}
    for r in records:
        if r["status"] == "completed":
            val = r.get(field_name)
            summary[val] = summary.get(val, 0) + r["total_amount"]
    return summary


def get_customers_with_multiple_orders(records):
    counts = count_by_field(records, "customer_name")
    return [cust for cust, count in counts.items() if count > 1]


def get_products_with_multiple_orders(records):
    counts = count_by_field(records, "product")
    return [prod for prod, count in counts.items() if count > 1]


def sort_key_total_amount(order):
    return order["total_amount"]


def sort_key_dictionary_value(item_tuple):
    return item_tuple[1]


def get_top_orders_by_total_amount(records, limit=5):
    completed = get_completed_orders(records)
    return sorted(completed, key=sort_key_total_amount, reverse=True)[:limit]


def get_top_elements_from_dict(summary_dict, limit=3):
    sorted_items = sorted(summary_dict.items(), key=sort_key_dictionary_value, reverse=True)
    return sorted_items[:limit]


def write_business_report(cleaned_valid_orders, invalid_orders):
    completed_orders = get_completed_orders(cleaned_valid_orders)
    completed_revenue = calculate_completed_revenue(cleaned_valid_orders)

    avg_val = completed_revenue / len(completed_orders) if completed_orders else 0.0
    highest = max((o["total_amount"] for o in completed_orders), default=0.0)
    lowest = min((o["total_amount"] for o in completed_orders), default=0.0)

    non_revenue_count = sum(1 for o in cleaned_valid_orders if o["status"] in ["pending", "cancelled", "returned"]
)

    rev_by_city = sum_revenue_by_field(cleaned_valid_orders, "city")
    rev_by_category = sum_revenue_by_field(cleaned_valid_orders, "category")
    rev_by_channel = sum_revenue_by_field(cleaned_valid_orders, "channel")
    rev_by_customer = sum_revenue_by_field(cleaned_valid_orders, "customer_name")
    rev_by_product = sum_revenue_by_field(cleaned_valid_orders, "product")

    top_5_orders = get_top_orders_by_total_amount(cleaned_valid_orders, 5)
    top_3_customers = get_top_elements_from_dict(rev_by_customer, 3)
    top_3_products = get_top_elements_from_dict(rev_by_product, 3)
    top_3_cities = get_top_elements_from_dict(rev_by_city, 3)

    with open("output/business_report.txt", "w", encoding="utf-8") as file:
        file.write("EXECUTIVE BUSINESS PERFORMANCE REPORT\n")
        file.write("=" * 50 + "\n\n")

        file.write("SECTION 1: KEY PERFORMANCE INDICATORS\n")
        file.write("-" * 50 + "\n")
        file.write(f"Total Completed Revenue: EUR {completed_revenue:,.2f}\n")
        file.write(f"Number of Completed Orders: {len(completed_orders)}\n")
        file.write(f"Non-Revenue Orders (pending/cancelled/returned): {non_revenue_count}\n")
        file.write(f"Invalid Records Removed: {len(invalid_orders)}\n")
        file.write(f"Average Order Size: EUR {avg_val:,.2f}\n")
        file.write(f"Highest Completed Order: EUR {highest:,.2f}\n")
        file.write(f"Lowest Completed Order: EUR {lowest:,.2f}\n\n")

        file.write("SECTION 2: PERFORMANCE BY DIMENSIONS\n")
        file.write("-" * 50 + "\n")
        file.write("Completed Revenue by City:\n")
        for city, rev in sorted(rev_by_city.items(), key=sort_key_dictionary_value, reverse=True):
            file.write(f"  - {city}: EUR {rev:,.2f}\n")

        file.write("\nCompleted Revenue by Category:\n")
        for cat, rev in sorted(rev_by_category.items(), key=sort_key_dictionary_value, reverse=True):
            file.write(f"  - {cat}: EUR {rev:,.2f}\n")

        file.write("\nCompleted Revenue by Channel:\n")
        for ch, rev in sorted(rev_by_channel.items(), key=sort_key_dictionary_value, reverse=True):
            file.write(f"  - {ch}: EUR {rev:,.2f}\n\n")

        file.write("SECTION 3: TOP RECORDS AND RANKINGS\n")
        file.write("-" * 50 + "\n")
        file.write("Top 5 Completed Orders by Value:\n")
        for o in top_5_orders:
            file.write(f"  - Order {o['order_id']} | {o['customer_name']} | {o['product']}: EUR {o['total_amount']:,.2f}\n")

        file.write("\nTop 3 Customers by Completed Revenue:\n")
        for cust, rev in top_3_customers:
            file.write(f"  - {cust}: EUR {rev:,.2f}\n")

        file.write("\nTop 3 Products by Completed Revenue:\n")
        for prod, rev in top_3_products:
            file.write(f"  - {prod}: EUR {rev:,.2f}\n")

        file.write("\nTop 3 Cities by Completed Revenue:\n")
        for city, rev in top_3_cities:
            file.write(f"  - {city}: EUR {rev:,.2f}\n\n")

        file.write("SECTION 4: DATA QUALITY INVESTIGATION\n")
        file.write("-" * 50 + "\n")
        file.write(f"- Removed {len(invalid_orders)} invalid records (missing names, 0 price/quantity).\n")
        file.write(f"- {non_revenue_count} valid orders are pending/cancelled/returned and excluded from revenue.\n")
        file.write("- Status inconsistencies before cleaning: 'Completed', 'complete' -> normalized to 'completed'.\n")
        file.write("- City inconsistency: 'Prishtine' -> normalized to 'Prishtina'.\n")
        file.write("- Category inconsistency: 'accessories' -> normalized to 'Accessories'.\n")
        file.write("- Channel inconsistency: 'Online' -> normalized to 'online'.\n")
        file.write("- Calculating revenue before validation would skew averages and include free/invalid orders.\n")
        file.write("- Counting pending/cancelled/returned as revenue would overstate income with money not received.\n\n")

        file.write("SECTION 5: STRATEGIC BUSINESS RECOMMENDATIONS\n")
        file.write("-" * 50 + "\n")
        file.write("1. Fix data entry: Add frontend validation to prevent empty names, zero prices, and\n")
        file.write("   negative quantities before orders are submitted.\n")
        file.write("2. Focus on top locations: Prishtina and Vushtrri drive the most revenue.\n")
        file.write("   Prioritize digital campaigns and stock in these cities.\n")


def main():
    # Part 1 - raw inspection
    print_raw_count(orders)
    print_first_three_records(orders)
    print_unique_raw_values(orders)

    # Part 2 - validation
    valid_orders, invalid_orders = split_valid_and_invalid_orders(orders)
    write_invalid_records(invalid_orders)

    # Part 3 - cleaning
    cleaned_valid_orders = []
    for order in valid_orders:
        cleaned_valid_orders.append(clean_order(order))

    write_validation_report(orders, valid_orders, invalid_orders, cleaned_valid_orders)

    print(f"\nValidation summary:")
    print(f"  Raw: {len(orders)} | Valid: {len(valid_orders)} | Invalid: {len(invalid_orders)}")

    print("\nInvalid orders:")
    for order in invalid_orders:
        print(f"  Order {order['order_id']}:")
        for reason in order["reasons"]:
            print(f"    - {reason}")

    cleaned_statuses = []
    cleaned_cities = []
    cleaned_categories = []
    cleaned_channels = []

    for order in cleaned_valid_orders:
        if order["status"] not in cleaned_statuses:
            cleaned_statuses.append(order["status"])
        if order["city"] not in cleaned_cities:
            cleaned_cities.append(order["city"])
        if order["category"] not in cleaned_categories:
            cleaned_categories.append(order["category"])
        if order["channel"] not in cleaned_channels:
            cleaned_channels.append(order["channel"])

    print("\nUnique values after cleaning:")
    print("  Statuses:", sorted(cleaned_statuses))
    print("  Cities:", sorted(cleaned_cities))
    print("  Categories:", sorted(cleaned_categories))
    print("  Channels:", sorted(cleaned_channels))

    # Part 4 - business metrics
    completed_orders = get_completed_orders(cleaned_valid_orders)

    non_revenue_count = 0
    for order in cleaned_valid_orders:
        if order["status"] in ["pending", "cancelled", "returned"]:
            non_revenue_count += 1

    completed_revenue = calculate_completed_revenue(cleaned_valid_orders)
    completed_count = len(completed_orders)

    if completed_count > 0:
        avg_completed_value = completed_revenue / completed_count
    else:
        avg_completed_value = 0.0

    if completed_orders:
        highest_order_value = max(order["total_amount"] for order in completed_orders)
        lowest_order_value = min(order["total_amount"] for order in completed_orders)
    else:
        highest_order_value = 0.0
        lowest_order_value = 0.0

    print("\nBusiness metrics:")
    print(f"  Raw records: {len(orders)}")
    print(f"  Valid records: {len(cleaned_valid_orders)}")
    print(f"  Invalid records: {len(invalid_orders)}")
    print(f"  Completed orders: {completed_count}")
    print(f"  Non-revenue orders: {non_revenue_count}")
    print(f"  Completed revenue: EUR {completed_revenue:.2f}")
    print(f"  Avg completed order value: EUR {avg_completed_value:.2f}")
    print(f"  Highest completed order: EUR {highest_order_value:.2f}")
    print(f"  Lowest completed order: EUR {lowest_order_value:.2f}")

    # Part 5 - dynamic reports
    orders_by_status = count_by_field(cleaned_valid_orders, "status")
    orders_by_city = count_by_field(cleaned_valid_orders, "city")
    orders_by_category = count_by_field(cleaned_valid_orders, "category")
    orders_by_channel = count_by_field(cleaned_valid_orders, "channel")

    rev_by_city = sum_revenue_by_field(cleaned_valid_orders, "city")
    rev_by_category = sum_revenue_by_field(cleaned_valid_orders, "category")
    rev_by_channel = sum_revenue_by_field(cleaned_valid_orders, "channel")
    rev_by_customer = sum_revenue_by_field(cleaned_valid_orders, "customer_name")

    mult_orders_cust = get_customers_with_multiple_orders(cleaned_valid_orders)
    mult_orders_prod = get_products_with_multiple_orders(cleaned_valid_orders)

    print("\nOrders by status:")
    for key, val in orders_by_status.items():
        print(f"  - {key}: {val}")

    print("\nOrders by city:")
    for key, val in orders_by_city.items():
        print(f"  - {key}: {val}")

    print("\nOrders by category:")
    for key, val in orders_by_category.items():
        print(f"  - {key}: {val}")

    print("\nOrders by channel:")
    for key, val in orders_by_channel.items():
        print(f"  - {key}: {val}")

    print("\nRevenue by city:")
    for key, val in rev_by_city.items():
        print(f"  - {key}: EUR {val:.2f}")

    print("\nRevenue by category:")
    for key, val in rev_by_category.items():
        print(f"  - {key}: EUR {val:.2f}")

    print("\nRevenue by channel:")
    for key, val in rev_by_channel.items():
        print(f"  - {key}: EUR {val:.2f}")

    print("\nRevenue by customer:")
    for key, val in rev_by_customer.items():
        print(f"  - {key}: EUR {val:.2f}")

    print("\nCustomers with multiple orders:")
    for cust in mult_orders_cust:
        print(f"  - {cust}")

    print("\nProducts ordered more than once:")
    for prod in mult_orders_prod:
        print(f"  - {prod}")

    # Part 6 - top records and ranking
    top_5_orders = get_top_orders_by_total_amount(cleaned_valid_orders, 5)
    top_3_cust = get_top_elements_from_dict(rev_by_customer, 3)

    rev_by_product = sum_revenue_by_field(cleaned_valid_orders, "product")
    top_3_products = get_top_elements_from_dict(rev_by_product, 3)
    top_3_cities = get_top_elements_from_dict(rev_by_city, 3)

    print("\nTop 5 completed orders by value:")
    for o in top_5_orders:
        print(f"  - Order {o['order_id']} | {o['customer_name']} | {o['product']}: EUR {o['total_amount']:.2f}")

    print("\nTop 3 customers by revenue:")
    for cust, rev in top_3_cust:
        print(f"  - {cust}: EUR {rev:.2f}")

    print("\nTop 3 products by revenue:")
    for prod, rev in top_3_products:
        print(f"  - {prod}: EUR {rev:.2f}")

    print("\nTop 3 cities by revenue:")
    for city, rev in top_3_cities:
        print(f"  - {city}: EUR {rev:.2f}")

    print("\nCategories by revenue (highest to lowest):")
    for cat, rev in sorted(rev_by_category.items(), key=sort_key_dictionary_value, reverse=True):
        print(f"  - {cat}: EUR {rev:.2f}")

    print("\nChannels by revenue (highest to lowest):")
    for ch, rev in sorted(rev_by_channel.items(), key=sort_key_dictionary_value, reverse=True):
        print(f"  - {ch}: EUR {rev:.2f}")

    # Part 7 - data quality investigation
    print("\nData quality check:")

    print("\n  Invalid records removed:")
    for order in invalid_orders:
        name = order['customer_name'] if order['customer_name'].strip() else "no name"
        print(f"    - order {order['order_id']} ({name}): {', '.join(order['reasons'])}")

    print(f"\n  Non-revenue valid orders: {non_revenue_count} (pending, cancelled, returned)")

    print("\n  Status values before normalization:")
    print("    - completed, Completed, complete, cancelled, pending, returned")

    print("\n  Values fixed during normalization:")
    print("    - Completed, complete -> completed")
    print("    - Prishtine -> Prishtina")
    print("    - accessories -> Accessories")
    print("    - Online -> online")

    print("\n  What goes wrong without validation:")
    print("    - revenue before validation includes price=0 and qty<=0 orders, breaks the average")
    print("    - counting pending/cancelled/returned inflates revenue with money never received")

    # Part 8 - generate output files
    write_business_report(cleaned_valid_orders, invalid_orders)
    print("\nreports saved to output/")


if __name__ == "__main__":
    main()