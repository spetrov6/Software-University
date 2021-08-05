word1 = input()
word2 = input()
word_one = list(word1)
word_two = list(word2)
count = 0
for i in word_two:
    if i != word_one[count]:
        word_one[count] = i
        print(*word_one,sep="")
    count += 1
