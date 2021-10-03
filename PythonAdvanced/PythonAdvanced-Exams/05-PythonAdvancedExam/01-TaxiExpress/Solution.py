from collections import deque

customers = deque([int(x) for x in input().split(", ")])
taxis = deque([int(x) for x in input().split(", ")])
total_time_passed = 0

while True:
    if len(customers) > 0:
        if len(taxis) > 0:
            if taxis[-1] >= customers[0]:
                total_time_passed += customers[0]
                taxis.pop()
                customers.popleft()
            else:
                taxis.pop()
        else:
            print("Not all customers were driven to their destinations")
            print(f"Customers left: {', '.join([str(x) for x in customers])}")
            break
    else:
        print("All customers were driven to their destinations")
        print(f"Total time: {total_time_passed} minutes")
        break

