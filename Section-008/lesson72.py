print("What is your age?")
age_str = input()

if age_str: #if age_str != "":
    age = int(age_str)

    if age >= 18 and age < 21:
        print("You can enter but you need a wristband!")
    elif age >= 21:
        print("You can enter and drink")
    else:
        print("You can't come in")
else:
    print("Please enter an age")
