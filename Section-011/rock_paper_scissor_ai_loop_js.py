from random import randint

print("Rock...")
print("Paper...")
print("Scissor...")
print("\n\n")

valid_values = ["rock", "paper", "scissors"]

def rps_game():
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
            print("Player 1 Wins!\n")
        elif player == "scissors" and computer == "paper":
            print("Player 1 Wins!\n")
        elif player == "paper" and computer == "rock":
            print("Player 1 Wins!\n")
        else:
            print("Sorry, you lost. :(\n")
            return False
        return True

game_counter = 0
user_wins = 0
while True:
    user_win = rps_game()
    if user_win:
        user_wins += 1
    game_counter += 1

    msg = input("Do you want to play again? (y/n) ")
    if(msg.lower() == "n"):
        break
