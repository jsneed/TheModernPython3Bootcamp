for x in range(1, 21):
    if x is 4 or x is 13:
        print(f"{x} is UNLUCKY!")
    elif x % 2 == 0:
        print(f"{x} is even")
    else:
        print(f"{x} is odd")
