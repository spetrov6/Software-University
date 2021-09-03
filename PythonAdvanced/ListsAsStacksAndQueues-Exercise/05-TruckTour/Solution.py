from collections import deque
pumps_count = int(input())
pumps = deque([input() for _ in range(pumps_count)])
total_fuel = 0
index = 0
counter = 0
start_point_found = False
while True:
    pump = pumps.popleft()
    fuel,kms = [int(x) for x in pump.split()]
    if fuel >= kms:
        pumps.appendleft(pump)
        for pump in pumps:
            fuel, kms = [int(x) for x in pump.split()]
            total_fuel += fuel
            if total_fuel >= kms:
                total_fuel -= kms
                counter += 1
            else:
                counter = 0
                total_fuel = 0
                pumps.append(pumps.popleft())
                index += 1
                break
        if counter >= len(pumps):
            start_point_found = True
    else:
        pumps.append(pump)
        index += 1
    if start_point_found:
        break
print(index)
