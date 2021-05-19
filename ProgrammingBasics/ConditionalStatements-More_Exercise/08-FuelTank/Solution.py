fuel = input()
fuel_amount = float(input())
if fuel == "Diesel":
    if fuel_amount >= 25:
        print(f"You have enough diesel.")
    else:
        print(f"Fill your tank with diesel!")
elif fuel == "Gasoline":
    if fuel_amount >= 25:
        print(f"You have enough gasoline.")
    else:
        print(f"Fill your tank with gasoline!")
elif fuel == "Gas":
    if fuel_amount >= 25:
        print(f"You have enough gas.")
    else:
        print(f"Fill your tank with gas!")
else:
    print("Invalid fuel!")