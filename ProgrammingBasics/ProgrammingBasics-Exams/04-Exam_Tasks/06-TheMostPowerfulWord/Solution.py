from math import  floor
word = input()
max_points = 0
points = 0
win_word = ""
vovews = ["a","A","e","E","i","I","o","O","u","U","y","Y"]
while word != "End of words":
    for i in word:
        points += ord(i)
    if word[0] in vovews:
        points = points * len(word)
    else:
        points = floor(points / len(word))
    if points > max_points:
        max_points = points
        win_word = word
    points = 0
    word = input()
print(f"The most powerful word is {win_word} - {max_points}")
