def is_num_palindrome(list_of_numbers):
    return list(map(lambda x: x == x[-1::-1],list_of_numbers))
[print(i) for i in is_num_palindrome(input().split(", "))]
