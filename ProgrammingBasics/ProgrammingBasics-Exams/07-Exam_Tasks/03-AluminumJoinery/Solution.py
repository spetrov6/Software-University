windows_count = int(input())
windows_type = input()
delivery_type = input()
total_price = 0
window_price = 0
if windows_count < 10:
    print("Invalid order")
else:
    if windows_type == "90X130":
        if 30 < windows_count <= 60:
            window_price = 110 - (110 * 0.05)
        elif windows_count > 60:
            window_price = 110 - (110 * 0.08)
        else:
            window_price = 110
    elif windows_type == "100X150":
        if 40 < windows_count <= 80:
            window_price = 140 - (140 * 0.06)
        elif windows_count > 80:
            window_price = 140 - (140 * 0.10)
        else:
            window_price = 140
    elif windows_type == "130X180":
        if 20 < windows_count <= 50:
            window_price = 190 - (190 * 0.07)
        elif windows_count > 50:
            window_price = 190 - (190 * 0.12)
        else:
            window_price = 190
    elif windows_type == "200X300":
        if 25 < windows_count <= 50:
            window_price = 250 - (250 * 0.09)
        elif windows_count > 50:
            window_price = 250 - (250 * 0.14)
        else:
            window_price = 250
    if delivery_type == "With delivery":
        total_price = windows_count * window_price + 60
    else:
        total_price = windows_count * window_price
    if windows_count > 99:
        total_price -= total_price * 0.04
    print(f"{total_price:.2f} BGN")