'''
Define a function called parse_date  that accepts a single string.  Your code should check to see if the 
string matches a date format.  We're going to use the DMY format of "dd/mm/yyyy", but it should also work with 
"dd.mm.yyyy" and "dd,mm,yyyy". If you are American, note that Day if before Month!  
However, rather than simply returning True or False if the string matches...you should instead return a dictionary containing the three 
parts of the date with the keys "d" , "m" , and "y"  like so:

parse_date("01/22/1999") # {'d': '01', 'm': '22', 'y': '1999'}

 Note: the string should be an EXACT match, containing the date and nothing else. If there is no match, return None

parse_date("12,04,2003") # {'d': '12', 'm': '04', 'y': '2003'}
parse_date("12.11.2003") # {'d': '12', 'm': '11', 'y': '2003'}
parse_date("12.11.200312") # None

'''
#import re
import re

#define parse_date below
def parse_date(msg):
    date_re = re.compile(r'^(?P<d>\d?\d)[\.\/,](?P<m>\d?\d)[\.\/,](?P<y>\d{4})$')
    result = date_re.search(msg)
    if result:
        return result.groupdict()
    else:
        return None

print(parse_date("01/22/1999"))       # {'d': '01', 'm': '22', 'y': '1999'}
print(parse_date("12,04,2003"))       # {'d': '12', 'm': '04', 'y': '2003'}
print(parse_date("12.11.2003"))       # {'d': '12', 'm': '11', 'y': '2003'}
print(parse_date("12.11.200312"))     # None
print(parse_date("reg 12.11.2003"))   # None
