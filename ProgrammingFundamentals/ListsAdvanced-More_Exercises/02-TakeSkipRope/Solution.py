encrypted_message = [i for i in input()]
numbers_list = [int(i) for i in encrypted_message if i.isdigit()]
encrypted_message = list(filter(lambda x: not x.isdigit(), encrypted_message))
take_list = [numbers_list[i] for i in range(len(numbers_list)) if i % 2 == 0]
skip_list = [numbers_list[i] for i in range(len(numbers_list)) if i % 2 != 0]
result_list = []
for _ in range(len(numbers_list) // 2):
    for i in range(take_list[0]):
        if len(encrypted_message) > 0:
            result_list.append(encrypted_message.pop(0))
    take_list.pop(0)
    for i in range(skip_list[0]):
        if len(encrypted_message) > 0:
            encrypted_message.pop(0)
    skip_list.pop(0)
print("".join(result_list))