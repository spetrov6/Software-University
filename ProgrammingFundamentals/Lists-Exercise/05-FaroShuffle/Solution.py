cards = input().split()
shuffles = int(input())
first_half = []
second_half = []
half = len(cards) // 2
for _ in range(shuffles):
    current_cards = []
    first_half = cards[0:half]
    second_half = cards[half::]
    for index in range(len(second_half)):
        current_cards.append(first_half[index])
        current_cards.append(second_half[index])
    cards = current_cards
print(cards)