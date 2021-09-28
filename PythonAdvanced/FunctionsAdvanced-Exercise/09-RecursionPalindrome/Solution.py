def palindrome(word,index=0,mirror_word=""):
    if index == 0:
        if len(mirror_word) == 0:
            index = len(word) - 1
    if index == -1:
        if word == mirror_word:
            return f"{word} is a palindrome"
        else:
            return f"{word} is not a palindrome"
    mirror_word += word[index]
    return palindrome(word,index-1,mirror_word)