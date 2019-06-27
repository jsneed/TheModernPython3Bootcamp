'''
Write a function called parse_bytes  that accepts a single string.  It should return a list of the binary 
bytes contained in the string.  Each byte is just a combination of eight 1's or 0's. For example:

parse_bytes("11010101 101 323")    # ['11010101']
parse_bytes("my data is: 10101010 11100010")    # ['10101010', '11100010']
parse_bytes("asdsa")   # []
Hints: take advantage of \b Not all bytes will have a space before and after, some come at the beginning of a file or at the end.  
Use findall!
    
'''

# don't forget to import re
import re 

# define parse_bytes below:
def parse_bytes(msg):
    byte_re = re.compile(r'\b[01]{8}\b')
    return byte_re.findall(msg)

print(parse_bytes("11010101 101 323"))                  # ['11010101']
print(parse_bytes("my data is: 10101010 11100010"))     # ['10101010', '11100010']
print(parse_bytes("asdsa"))                             # []