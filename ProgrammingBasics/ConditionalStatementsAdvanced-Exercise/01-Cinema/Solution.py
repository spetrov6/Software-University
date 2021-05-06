projection_tipe = input()
r = int(input())
c = int(input())
places = r * c
projection = {"Premiere": 12.00, "Normal": 7.50, "Discount": 5}
for key,value in projection.items():
    if projection_tipe == key:
       price = places * value
       print(f"{price:0.3f} leva")
       break