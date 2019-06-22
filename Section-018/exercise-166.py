'''
multiple_letter_count("awesome") # {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}
'''

# flesh out multiple_letter count:
def multiple_letter_count(msg):
    return {char : msg.count(char) for char in msg}

print(multiple_letter_count("awesome"))
print(multiple_letter_count("hello"))
