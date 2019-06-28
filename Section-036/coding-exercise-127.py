'''
Write a function called is_odd_string which returns true if sum of each character's position in the alphabet is odd. For example, "a" is 
in the first position, "b" is in the second position, and so on. If the sum is even, return false.  NOTE: INDEXING STARTS AT 1.  A is 
position 1, NOT POSITION 0.

is_odd_string('a') # True
is_odd_string('aaaa') # False
is_odd_string('amazing') # True
is_odd_string('veryfun') # True
is_odd_string('veryfunny') # False
'''

def is_odd_string(msg):
    sum_word = 0
    chars = [chr(i).lower() for i in range(65,91) ]
    alphabet = dict(zip(chars, [j for j in range(1, 27)]))
    for x in msg:
        sum_word += alphabet[x]
    return sum_word % 2 != 0



print(is_odd_string('a')) # True
print(is_odd_string('aaaa')) # False
print(is_odd_string('amazing')) # True
print(is_odd_string('veryfun')) # True
print(is_odd_string('veryfunny')) # False