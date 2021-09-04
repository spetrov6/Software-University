from collections import deque
green_light_duration = int(input())
free_window_duration = int(input())
cars_waiting = deque()
current_car_passing = deque()
current_car_brand = ""
passed_cars_count = 0
crash = False
car_brand = input()
while car_brand != "END":
    time_passed = 0
    if car_brand != "green":
        cars_waiting.append(deque(car_brand))
    else:
        while time_passed <= green_light_duration + free_window_duration:
            time_passed += 1
            if time_passed <= green_light_duration and len(current_car_passing) == 0 and len(cars_waiting) > 0:
                current_car_passing = cars_waiting.popleft()
                current_car_brand = "".join(current_car_passing)
                passed_cars_count += 1
            if time_passed <= green_light_duration + free_window_duration:
                if len(current_car_passing) > 0:
                    current_car_passing.popleft()
        if len(current_car_passing) > 0:
            crash = True
    if crash:
        print("A crash happened!")
        print(f"{current_car_brand} was hit at {current_car_passing.popleft()}.")
        break
    car_brand = input()
if not crash:
    print("Everyone is safe.")
    print(f"{passed_cars_count} total cars passed the crossroads.")