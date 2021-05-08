text = input()
letters_values = {"a":1,"e":2,"i":3,"o":4,"u":5}
result = 0
for key in text:
    if key in letters_values:
        result += letters_values[key]
print(result)
