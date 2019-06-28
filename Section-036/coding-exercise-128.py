'''
Write a function called valid_parentheses that takes a string of parentheses, and determines if the order of the parentheses is valid. 
valid_parentheses should return true if the string is valid, and false if it's invalid.

valid_parentheses("()") # True 
valid_parentheses(")(()))") # False 
valid_parentheses("(") # False 
valid_parentheses("(())((()())())") # True 
valid_parentheses('))((') # False
valid_parentheses('())(') # False
valid_parentheses('()()()()())()(') # False
'''

def valid_parentheses(parens):
    temp = []
    for i in parens:
        if i == '(':
            temp.insert(0, '(')
        elif i == ')':
            try:
                temp.remove('(')
            except ValueError  as err:
                return False
    if(len(temp) == 0): return True
    return False

print(valid_parentheses("()")) # True 
print(valid_parentheses(")(()))")) # False 
print(valid_parentheses("(")) # False 
print(valid_parentheses("(())((()())())")) # True 
print(valid_parentheses('))((')) # False
print(valid_parentheses('())(')) # False
print(valid_parentheses('()()()()())()(')) # False