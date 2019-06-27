'''
Write a function called is_valid_time that accepts a single string argument. It should return True
if the string is formatted correctly as a time, like 3:15 or 12:48 and return False otherwise.  Note that times can start with 
a single number (2:30) or two (11:18).  

In order to return True, the string should ONLY contain the time, and no other characters
Don't worry about impossible times like 88:76, just focus on the formatting!

is_valid_time("10:45") #True
'''

import re

# Define is_valid_time below:
def is_valid_time(message):
    time_re = re.compile(r'^\d{1,2}\:\d{2}$')
    matches = time_re.findall(message)
    if len(matches) > 0:
        return True
    else:
        return False

print(is_valid_time("10:45"))          # True
print(is_valid_time("it it 10:45"))    # False
print(is_valid_time("11:45"))          # True
print(is_valid_time("88:45"))          # True
print(is_valid_time("188:45"))         # False
print(is_valid_time("18845"))          # False
