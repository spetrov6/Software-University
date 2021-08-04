number_of_guest = int(input())
guests = set()
guest_come = set()
for _ in range(number_of_guest):
    guests.add(input())
code = input()
while code != "END":
    guest_come.add(code)
    code = input()
dont_come = guests.difference(guest_come)
dont_come_dict = {"VIP":[],"Regular":[]}
for status in dont_come:
    if status[0].isdigit():
        dont_come_dict["VIP"].append(status)
    else:
        dont_come_dict["Regular"].append(status)
print(len(dont_come))
for key,value in dont_come_dict.items():
    dont_come_dict[key] = sorted(value)
[[print(x) for x in value] for key,value in dont_come_dict.items()]