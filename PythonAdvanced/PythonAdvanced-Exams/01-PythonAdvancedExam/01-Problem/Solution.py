from collections import deque


def check_order_validity():
    if order <= 0 or order > 10:
        return False
    return True


def check_orders_and_workers_count(orders, employees):
    if not orders:
        orders = False
    elif not employees:
        employees = False
    return orders, employees


pizza_orders = deque([int(x) for x in input().split(", ")])
employees_capacity = deque([int(x) for x in input().split(", ")])
pizzas_made = 0


while True:
    pizza_orders, employees_capacity = check_orders_and_workers_count(pizza_orders, employees_capacity)

    if pizza_orders and employees_capacity:
        order = pizza_orders.popleft()

        if check_order_validity():
            worker_capacity = employees_capacity.pop()

            if order <= worker_capacity:
                pizzas_made += order

            else:
                pizzas_made += worker_capacity
                order -= worker_capacity
                pizza_orders.appendleft(order)

    else:
        if employees_capacity:
            print("All orders are successfully completed!")
            print(f"Total pizzas made: {pizzas_made}")
            print(f"Employees: {', '.join([str(x) for x in employees_capacity])}")
            break

        else:
            print("Not all orders are completed.")
            print(f"Orders left: {', '.join([str(x) for x in pizza_orders])}")
            break
