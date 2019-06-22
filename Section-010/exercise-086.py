num = input("How many times do I have to tell you: ")

phrase = "Clean your room!"

if num:
    times = int(num)
    for x in range(times):
        print(phrase.upper())
