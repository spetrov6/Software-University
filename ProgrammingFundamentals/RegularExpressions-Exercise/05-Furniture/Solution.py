import re
text = input()
pattern = r">>(?P<furniture>[a-z]+)<<(?P<price>[0-9]+(\.[0-9]+)?)!(?P<quantity>[0-9]+)"
result = []
while not text == "Purchase":
    result.extend([obj.groupdict() for obj in re.finditer(pattern,text,re.IGNORECASE)])
    text = input()
total_price = 0
print(f"Bought furniture:")
for i in result:
    print(f'{i.get("furniture")}')
    total_price += float(i.get("price")) * int(i.get("quantity"))
print(f"Total money spend: {total_price:.2f}")