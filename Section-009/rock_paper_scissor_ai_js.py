from random import randint

print("Rock...")
print("Paper...")
print("Scissor...")

valid_values = ["rock", "paper", "scissors"]
x = randint(0, 2)
computer = valid_values[x]

player = input("Player please make your move: ").lower()
print(f"The computer chose {computer}.")

if not player or player not in valid_values:
    print("You didn't enter a valid value.")
else:
    player = player
    if player == computer:
        print("It's a tie")
    elif player == "rock" and computer == "scissors":
        print("Player 1 Wins!")
    elif player == "scissors" and computer == "paper":
        print("Player 1 Wins!")
    elif player == "paper" and computer == "rock":
        print("Player 1 Wins!")
    else:
        print("Sorry, you lost. :(")
