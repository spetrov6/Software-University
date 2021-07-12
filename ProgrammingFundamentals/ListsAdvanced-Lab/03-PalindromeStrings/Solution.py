palindromes = [i for i in input().split() if i == i[::-1]]
searched_word = input()
print(palindromes)
print(f"Found palindrome {palindromes.count(searched_word)} times")