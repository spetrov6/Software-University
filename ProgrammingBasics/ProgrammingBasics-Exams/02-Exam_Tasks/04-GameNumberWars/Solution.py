player1 = input()
player2 = input()
card = input()
player1_points = 0
player2_points = 0
while card != "End of game":
    card1 = int(card)
    card2 = int(input())
    if card1 > card2:
        player1_points += card1 - card2
    elif card1 < card2:
        player2_points += card2 - card1
    else:
        print("Number wars!")
        card1 = int(input())
        card2 = int(input())
        if card1 > card2:
            print(f"{player1} is winner with {player1_points} points")
            break
        else:
            print(f"{player2} is winner with {player2_points} points")
            break
    card = input()
if card == "End of game":
    print(f"{player1} has {player1_points} points")
    print(f"{player2} has {player2_points} points")
