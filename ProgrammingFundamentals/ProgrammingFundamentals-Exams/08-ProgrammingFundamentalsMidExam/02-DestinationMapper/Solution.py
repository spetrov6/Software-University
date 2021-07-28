import re
whole_string = input()
pattern = r'(?<=(?P<sep>(=|/)))[A-Z][A-Za-z]{2,}(?=(?P=sep))'
stops = []
stops_count = 0
for stop in re.finditer(pattern,whole_string):
    stops.append(stop.group())
for stop in stops:
    stops_count += len(stop)
print(f"Destinations: {', '.join(stops)}")
print(f"Travel Points: {stops_count}")
