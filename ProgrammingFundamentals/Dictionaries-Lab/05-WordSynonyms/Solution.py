number_of_words = int(input())
words_dictionary = {}
for _ in range(number_of_words):
    word = input()
    synonym = input()
    if word  not in words_dictionary:
        words_dictionary[word] = []
    words_dictionary[word].append(synonym)
[print(f"{key} - {', '.join(value)}") for (key,value) in words_dictionary.items()]