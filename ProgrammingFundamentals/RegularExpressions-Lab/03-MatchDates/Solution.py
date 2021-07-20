import re
dates = input()
pattern = r"\b(?P<Day>\d\d)(?P<sep>(\.|-|/))(?P<month>[A-Z]\D{2})(?P=sep)(?P<year>\d{4})\b"
result = [obj.groupdict() for obj in re.finditer(pattern,dates)]
for el in result:
    print(f'Day: {el.get("Day")}, Month: {el.get("month")}, Year: {el.get("year")}')