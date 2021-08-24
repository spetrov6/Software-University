def characters_count_function(char,all_char):
    characters_count = {}
    for i in char:
        characters_count[i] = all_char.count(i)
    [print(f"{key} -> {value}") for key,value in characters_count.items()]
characters_as_string = [i for i in input() if i != " "]
characters = []
characters = [i for i in characters_as_string if i != " " and i not in characters]
characters_count_function(characters,characters_as_string)