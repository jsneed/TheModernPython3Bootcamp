'''
capitalize("tim") # "Tim"
capitalize("matt") # "Matt"
'''

def capitalize(msg):
    if len(msg) > 0:
        char = msg[0:1]
        return char.upper() + msg[1:]

print(capitalize("tim"))
print(capitalize("matt"))
