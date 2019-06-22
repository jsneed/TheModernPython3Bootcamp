from random import randint


def guessingGame(num, guess_str):
    guess = int(guess_str)
    while guess != num:
        if guess < num:
            state = "Higher"
        else:
            state = "Lower"
        guess_str = input(f"{state}, guess again: ")
        guess = int(guess_str)
    print("You Win!")
    print()


end_game = False
while not end_game:
    guess = input("What is your guess? ")
    guessingGame(randint(1, 10), guess)
    msg = input("Do you want to play again (y/n)? ")
    if msg.lower() == "n":
        break
