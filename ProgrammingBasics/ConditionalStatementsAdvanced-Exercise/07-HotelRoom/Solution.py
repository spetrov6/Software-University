month = input()
nights = int(input())

if month == "May" or month == "October":
    apartment = nights * 65
    studio = nights * 50
    if nights > 7 and nights <= 14:
        studio = studio - (studio * 0.05)
    elif nights > 14:
        studio = studio - (studio * 0.30)
elif month == "June" or month == "September":
    studio = nights * 75.20
    apartment = nights * 68.70
    if nights > 14:
        studio = studio - (studio * 0.20)
else:
    studio = nights * 76
    apartment = nights *77
if nights > 14:
    apartment = apartment - (apartment * 0.10)
print(f"Apartment: {apartment:.2f} lv."f"\nStudio: {studio:.2f} lv.")