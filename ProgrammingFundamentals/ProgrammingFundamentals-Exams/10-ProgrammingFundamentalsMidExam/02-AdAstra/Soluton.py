import re
pattern = r"(?P<separator>(#|\|))(?P<food>([a-zA-Z]| )+)+(?P=separator)" \
          r"(?P<bestby>\d{2}/\d{2}/\d{2})(?P=separator)(?P<calories>\d+)(?P=separator)"
string = input()
food = [obj.groupdict() for obj in re.finditer(pattern,string)]
total_days = 0
for item in food:
    total_days += int(item.get("calories"))
total_days = total_days // 2000
print(f"You have food to last you for: {total_days} days!")
for item in food:
    print(f'Item: {item.get("food")}, Best before: {item.get("bestby")}, Nutrition: {item.get("calories")}')