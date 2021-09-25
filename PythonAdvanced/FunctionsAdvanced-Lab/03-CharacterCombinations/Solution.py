from itertools import permutations
result = list(permutations(input()))
[print(''.join(x)) for x in result]