orders = [
    {
        "order_id": 1,
        "customer_name": "Arta",
        "city": "Vushtrri",
        "product": "Laptop",
        "category": "Electronics",
        "quantity": 1,
        "price": 700,
        "status": "completed",
        "order_date": "2026-07-01"
    },
    {
        "order_id": 2,
        "customer_name": "Blend",
        "city": "Prishtina",
        "product": "Mouse",
        "category": "Accessories",
        "quantity": 2,
        "price": 15,
        "status": "completed",
        "order_date": "2026-07-01"
    },
    {
        "order_id": 3,
        "customer_name": "Arta",
        "city": "Vushtrri",
        "product": "Keyboard",
        "category": "Accessories",
        "quantity": 1,
        "price": 40,
        "status": "cancelled",
        "order_date": "2026-07-02"
    },
    {
        "order_id": 4,
        "customer_name": "Dren",
        "city": "Mitrovica",
        "product": "Monitor",
        "category": "Electronics",
        "quantity": 1,
        "price": 180,
        "status": "completed",
        "order_date": "2026-07-02"
    },
    {
        "order_id": 5,
        "customer_name": "Elira",
        "city": "Prishtina",
        "product": "Mouse",
        "category": "Accessories",
        "quantity": 1,
        "price": 15,
        "status": "completed",
        "order_date": "2026-07-03"
    },
    {
        "order_id": 6,
        "customer_name": "Dren",
        "city": "Mitrovica",
        "product": "Laptop",
        "category": "Electronics",
        "quantity": 1,
        "price": 700,
        "status": "pending",
        "order_date": "2026-07-03"
    },
    {
        "order_id": 7,
        "customer_name": "Nora",
        "city": "Vushtrri",
        "product": "Headphones",
        "category": "Accessories",
        "quantity": 1,
        "price": 50,
        "status": "completed",
        "order_date": "2026-07-04"
    },
    {
        "order_id": 8,
        "customer_name": "Leart",
        "city": "Peja",
        "product": "Monitor",
        "category": "Electronics",
        "quantity": 2,
        "price": 180,
        "status": "completed",
        "order_date": "2026-07-04"
    },
    {
        "order_id": 9,
        "customer_name": "Faton",
        "city": "Prizren",
        "product": "Desk Chair",
        "category": "Office",
        "quantity": 1,
        "price": 120,
        "status": "completed",
        "order_date": "2026-07-05"
    },
    {
        "order_id": 10,
        "customer_name": "Gresa",
        "city": "Prishtina",
        "product": "USB Cable",
        "category": "Accessories",
        "quantity": 3,
        "price": 8,
        "status": "completed",
        "order_date": "2026-07-05"
    },
    {
        "order_id": 11,
        "customer_name": "Rina",
        "city": "Vushtrri",
        "product": "Laptop",
        "category": "Electronics",
        "quantity": 1,
        "price": 650,
        "status": "cancelled",
        "order_date": "2026-07-06"
    },
    {
        "order_id": 12,
        "customer_name": "Arben",
        "city": "Ferizaj",
        "product": "Desk",
        "category": "Office",
        "quantity": 1,
        "price": 220,
        "status": "pending",
        "order_date": "2026-07-06"
    }
]

def print_basic_data(orders):
    print(f"\nTotal orders: {len(orders)}")
    
    print("\nCustomer names:")
    for order in orders:
        print(order.get("customer_name"))

    
    print("\nOrder details:")
    for order in orders:
        print(f"{order.get('customer_name')} ordered {order.get('product')} from {order.get('city')} and the status is {order.get('status')}")


print_basic_data(orders)

print("________________________________________\n")

def filter_by_status(orders, status):
    result = []

    for order in orders:
        if order["status"] == status:
            result.append(order)

    return result


print("\nCompleted orders:")

for order in filter_by_status(orders, "completed"):
    print(
        order["order_id"],
        "-",
        order["customer_name"],
        "-",
        order["product"]
    )


print("\nPending orders:")

for order in filter_by_status(orders, "pending"):
    print(
        order["order_id"],
        "-",
        order["customer_name"],
        "-",
        order["product"]
    )


print("\nCancelled orders:")

for order in filter_by_status(orders, "cancelled"):
    print(
        order["order_id"],
        "-",
        order["customer_name"],
        "-",
        order["product"]
    )

def filter_by_price(orders, price):

    result = []

    for order in orders:
        if order["price"] > price:
            result.append(order)

    return result

print("\nPrice greater than 100:")



for order in filter_by_price(orders, 100):
    print(
        order["customer_name"],
        "-",
        order["product"],
        "-",
        order["price"]
    )
    
    
def filter_by_category(orders, category):

    result = []

    for order in orders:
        if order["category"] == category:
            result.append(order)

    return result

print("\nAccessories:")

for order in filter_by_category(orders, "Accessories"):
    print(
        order["customer_name"],
        "-",
        order["product"]
    )















def calculate_totals(orders):

    result = []

    for order in orders:

        total_amount = order["quantity"] * order["price"]

        result.append({
            "customer_name": order["customer_name"],
            "product": order["product"],
            "quantity": order["quantity"],
            "price": order["price"],
            "total_amount": total_amount
        })

    return result



totals = calculate_totals(orders)


print("\nOrder totals:")

for order in totals:
    print(
        f"{order['customer_name']} - "
        f"{order['product']} - "
        f"{order['quantity']} x "
        f"{order['price']} = "
        f"{order['total_amount']}"
    )




sorted_by_price = orders.copy()


for i in range(len(sorted_by_price)):

    for j in range(i + 1, len(sorted_by_price)):

        if sorted_by_price[i]["price"] < sorted_by_price[j]["price"]:

            temp = sorted_by_price[i]
            sorted_by_price[i] = sorted_by_price[j]
            sorted_by_price[j] = temp


print("\nOrders sorted by price:")

for order in sorted_by_price:
    print(
        order["customer_name"],
        "-",
        order["product"],
        "-",
        order["price"]
    )



sorted_by_total = totals.copy()


for i in range(len(sorted_by_total)):

    for j in range(i + 1, len(sorted_by_total)):

        if sorted_by_total[i]["total_amount"] < sorted_by_total[j]["total_amount"]:

            temp = sorted_by_total[i]
            sorted_by_total[i] = sorted_by_total[j]
            sorted_by_total[j] = temp


print("\nTop 3 orders by total amount:")

for order in sorted_by_total[:3]:
    print(
        order["customer_name"],
        "-",
        order["product"],
        "-",
        order["total_amount"]
    )



def status_summary(orders):

    counts = {}

    for order in orders:

        status = order["status"]

        if status not in counts:
            counts[status] = 0

        counts[status] += 1

    return counts



status_counts = status_summary(orders)


print("\nStatus counts:")

for status, count in status_counts.items():
    print(status, ":", count)



def completed_revenue(orders):

    total = 0

    for order in orders:

        if order["status"] == "completed":

            total += order["quantity"] * order["price"]

    return total



print(
    "\nCompleted revenue:",
    completed_revenue(orders)
)



def customer_orders_count(orders):

    customers = {}

    for order in orders:

        name = order["customer_name"]

        if name not in customers:
            customers[name] = 0

        customers[name] += 1

    return customers



print("\nCustomers with more than one order:")

customer_counts = customer_orders_count(orders)

for customer, count in customer_counts.items():

    if count > 1:
        print(customer, "-", count, "orders")
        
        
        

# Part 4 - Mini Business Challenge


def most_expensive_order(orders):

    expensive_order = orders[0]

    for order in orders:

        total = order["quantity"] * order["price"]

        expensive_total = (
            expensive_order["quantity"] *
            expensive_order["price"]
        )

        if total > expensive_total:
            expensive_order = order

    return expensive_order



expensive = most_expensive_order(orders)


print("\nMost expensive single order:")

print(
    expensive["customer_name"],
    "-",
    expensive["product"],
    "-",
    expensive["quantity"] * expensive["price"]
)




def highest_total_amount(orders):

    highest_order = orders[0]

    for order in orders:

        current_total = order["quantity"] * order["price"]

        highest_total = (
            highest_order["quantity"] *
            highest_order["price"]
        )

        if current_total > highest_total:
            highest_order = order

    return highest_order



highest = highest_total_amount(orders)


print("\nHighest total amount order:")

print(
    highest["customer_name"],
    "-",
    highest["product"],
    "-",
    highest["quantity"] * highest["price"]
)




def not_real_revenue(orders):

    result = []

    for order in orders:

        if order["status"] == "pending" or order["status"] == "cancelled":
            result.append(order)

    return result



print("\nOrders NOT counted as revenue:")

for order in not_real_revenue(orders):

    print(
        order["customer_name"],
        "-",
        order["product"],
        "-",
        order["status"]
    )




def calculate_completed_revenue(orders):

    total = 0

    for order in orders:

        if order["status"] == "completed":

            total += order["quantity"] * order["price"]

    return total



print("\nCompleted revenue:")

print(calculate_completed_revenue(orders))




print("\nBusiness Answer:")

print(
    f"The most valuable order is {highest['product']} from {highest['customer_name']} with a total amount of {highest['quantity'] * highest['price']}."
)

print(
    "Cancelled orders should not be counted as revenue because they are not completed sales."
)