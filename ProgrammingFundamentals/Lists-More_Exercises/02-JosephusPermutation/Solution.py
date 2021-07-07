sequence = [int(i) for i in input().split()]
number_of_jumps = int(input())
result = []
counter = 1
index = 0
while len(sequence) > 0:
    if index >= len(sequence):
        index = 0
    if counter % number_of_jumps == 0:
        result.append(sequence[index])
        sequence.pop(index)
        index -= 1
    counter += 1
    index += 1
print(str(result).replace(' ', '').replace('\'', ''))