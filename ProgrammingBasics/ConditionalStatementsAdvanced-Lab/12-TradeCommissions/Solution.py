city = input()
sales = float(input())
if city == "Sofia":
    if sales >= 0 and sales <= 500:
        print(f"{sales * 0.05:0.2f}")
    elif sales > 500 and sales <= 1000:
        print(f"{sales * 0.07:0.2f}")
    elif sales > 1000 and sales <= 10000:
        print(f"{sales * 0.08:0.2f}")
    elif sales > 10000:
        print(f"{sales * 0.12:0.2f}")
    else:
        print("error")
elif city == "Varna":
    if sales >= 0 and sales <= 500:
        print(f"{sales * 0.045:0.2f}")
    elif sales > 500 and sales <= 1000:
        print(f"{sales * 0.075:0.2f}")
    elif sales > 1000 and sales <= 10000:
        print(f"{sales * 0.10:0.2f}")
    elif sales > 10000:
        print(f"{sales * 0.13:0.2f}")
    else:
        print("error")
elif city == "Plovdiv":
    if sales >= 0 and sales <= 500:
        print(f"{sales * 0.055:0.2f}")
    elif sales > 500 and sales <= 1000:
        print(f"{sales * 0.08:0.2f}")
    elif sales > 1000 and sales <= 10000:
        print(f"{sales * 0.12:0.2f}")
    elif sales > 10000:
        print(f"{sales * 0.145:0.2f}")
    else:
        print("error")
else:
    print("error")
