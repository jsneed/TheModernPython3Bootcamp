# Lesson 59
conversion = 1.60934 #how many kilos equal a mile
print("How many kilometers do you want to convert?")
k_str = input()
print(f"You said {k_str}")
kilometers = float(k_str)
miles = round(kilometers / conversion, 2)
print(f"That is {miles} miles.")
