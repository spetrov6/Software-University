n = int(input())
max_result = 0
for i in range(n):
    snow = int(input())
    time = int(input())
    quality = int(input())
    result = (snow / time) ** quality
    if result > max_result:
        max_result = result
        max_quality = quality
        max_snow = snow
        max_time = time
        max_value = snow / time
print(f"{max_snow} : {max_time} = {int(max_value ** max_quality)} ({max_quality})")