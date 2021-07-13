employee_happiness = list(map(lambda x: int(x), input().split()))
improvement_factor = int(input())
total_happiness = list(map(lambda x: x * improvement_factor,employee_happiness))
#happiest_employee = [i for i in total_happiness if i >= (sum(total_happiness) / len(total_happiness))]
happiest_employee = list(filter(lambda x: x >= (sum(total_happiness) / len(total_happiness)),total_happiness))
if len(happiest_employee) >= len(total_happiness) // 2:
    print(f"Score: {len(happiest_employee)}/{len(total_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happiest_employee)}/{len(total_happiness)}. Employees are not happy!")