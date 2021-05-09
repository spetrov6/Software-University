n = int(input())
salary = int(input())
for i in range(n):
    site = input()
    if salary > 0 and i < n:
        if site == "Facebook":
            salary -= 150
        elif site == "Instagram":
            salary -= 100
        elif site == "Reddit":
            salary -= 50
    if salary <= 0:
        print("You have lost your salary.")
        break
    if i + 1 == n:
        print(salary)
        break


