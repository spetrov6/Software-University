company_as_string = input()
company_info = {}
while company_as_string != "End":
    company,employee = company_as_string.split(" -> ")
    if company not in company_info:
        company_info[company] = []
    if employee not in company_info[company]:
        company_info[company].append(employee)
    company_as_string = input()
for key,value in sorted(company_info.items()):
    print(key)
    for j in value:
        print(f"-- {j}")