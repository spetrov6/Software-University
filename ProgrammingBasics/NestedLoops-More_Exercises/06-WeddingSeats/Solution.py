last_sector = ord(input())
row_first = int(input())
odd_places = int(input())
places_count = 0
for sector in range(65, last_sector + 1):
    for row in range(1, row_first + 1):
        if row % 2 != 0:
            places_range = odd_places
        elif row % 2 == 0:
            places_range = odd_places + 2
        for place in range(1, places_range + 1):
            print(f"{chr(sector)}{row}{chr(place + 96)}")
            places_count += 1
    row_first += 1
print(places_count)