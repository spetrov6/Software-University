data = input().split()
total_number = 0
for i in data:
    first_letter = i[0]
    last_letter = i[-1]
    number = int(i[1:-1])
    if first_letter.isupper():
        number = number / (ord(first_letter.lower()) - 96)
    elif first_letter.islower():
        number = int(number) * (ord(first_letter) - 96)
    if last_letter.isupper():
        number = number - (ord(last_letter.lower()) - 96)
    elif last_letter.islower():
        number = number + (ord(last_letter) - 96)
    total_number += number
print(f"{total_number:.2f}")