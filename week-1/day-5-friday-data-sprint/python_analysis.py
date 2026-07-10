import csv


def load_orders():
    orders = []

    with open("data/orders.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["quantity"] = int(row["quantity"])
            row["price"] = float(row["price"])

            orders.append(row)

    return orders


def calculate_total_amount(order):
    return order["quantity"] * order["price"]


def get_completed_orders(orders):
    completed_orders = []

    for order in orders:
        if order["status"] == "completed":
            completed_orders.append(order)

    return completed_orders


def get_non_revenue_orders(orders):
    non_revenue_orders = []

    for order in orders:
        if order["status"] == "pending" or order["status"] == "cancelled":
            non_revenue_orders.append(order)

    return non_revenue_orders


def calculate_completed_revenue(orders):
    revenue = 0

    for order in orders:
        if order["status"] == "completed":
            revenue += calculate_total_amount(order)

    return revenue


def find_most_expensive_order(orders):
    if not orders:
        return None

    expensive_order = orders[0]

    for order in orders:
        if order["price"] > expensive_order["price"]:
            expensive_order = order

    return expensive_order


def find_highest_total_amount_order(orders):
    if not orders:
        return None

    highest_order = orders[0]

    for order in orders:
        if calculate_total_amount(order) > calculate_total_amount(highest_order):
            highest_order = order

    return highest_order


def count_by_status(orders):
    counts = {}

    for order in orders:
        status = order["status"]

        if status in counts:
            counts[status] += 1
        else:
            counts[status] = 1

    return counts


def count_by_city(orders):
    counts = {}

    for order in orders:
        city = order["city"]

        if city in counts:
            counts[city] += 1
        else:
            counts[city] = 1

    return counts


def count_by_category(orders):
    counts = {}

    for order in orders:
        category = order["category"]

        if category in counts:
            counts[category] += 1
        else:
            counts[category] = 1

    return counts


def print_business_report(orders):

    completed_orders = get_completed_orders(orders)
    non_revenue_orders = get_non_revenue_orders(orders)


    print(f"Total Orders: {len(orders)}")
    print("\nCompleted Orders:")
    for order in completed_orders:
        print(
            f"{order['customer_name']} - {order['product']} - {order['status']} ")

    print(f"\nPending/Cancelled Orders:")
    for order in non_revenue_orders:
        print(
            f"{order['customer_name']} - {order['product']} - {order['status']} ")
    print(f"\nCompleted Revenue: {calculate_completed_revenue(orders)}")


   

    expensive = find_most_expensive_order(orders)

    if expensive:
        print("\nMost Expensive Single Order:")
        print(
            f"{expensive['customer_name']} - {expensive['product']} - {expensive['price']}")

    highest = find_highest_total_amount_order(orders)

    if highest:
        print("\nHighest Total Amount Order:")
        print(
            f"{highest['customer_name']} - {highest['product']} - {calculate_total_amount(highest)}")


    print("\nOrders By Status:")
    for status, count in count_by_status(orders).items():
        print(f"{status}: {count}")


    print("\nOrders By City:")
    for city, count in count_by_city(orders).items():
        print(f"{city}: {count}")


    print("\nOrders By Category:")
    for category, count in count_by_category(orders).items():
        print(f"{category}: {count}")


    print("\nOrders Not Counted As Revenue:")

    for order in non_revenue_orders:
        print(
            f"{order['customer_name']} - {order['product']} - {order['status']}"
        )

def main():
    orders = load_orders()
    print_business_report(orders)


if __name__ == "__main__":
    main()