num_sequence = [int(i) for i in input().split()]
avarage_num = sum(num_sequence) / len(num_sequence)
less = True
for _ in range(5):
       if max(num_sequence) > avarage_num:
            print(max(num_sequence),end=" ")
            num_sequence.pop(num_sequence.index(max(num_sequence)))
            less = False
if less:
    print("No")