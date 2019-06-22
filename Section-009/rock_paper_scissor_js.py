print("Rock...")
print("Paper...")
print("Scissor...")

player1 = input("Player 1 make your move: ")

for x in range(40):
    print("*** NO CHEATING! ***")

player2 = input("Player 2 make your move: ")

if player1 and player2:
    if player1 == player2:
        print("It's a draw")
    elif player1 == "rock":
        if player2 == "scissor":
            print("Player 1 Wins!")
        else:
            print("Player 2 Wins!")
    elif player1 == "scissor":
        if player2 == "paper":
            print("Player 1 Wins!")
        else:
            print("Player 2 Wins!")
    elif player1 == "paper":
        if player2 == "rock":
            print("Player 1 Wins!")
        else:
            print("Player 2 Wins!")
