numbers = list(map(lambda x: int(x),input().split(", ")))
group = 10
while len(numbers) > 0:
    list_to_print = []
    for i in numbers:
        if i <= group:
            list_to_print.append(i)
    for i in list_to_print:
        numbers.remove(i)
    print(f"Group of {group}'s: {list_to_print}")
    group += 10