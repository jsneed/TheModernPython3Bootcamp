'''
Exercise Involving Closures

Write a function called letter_counter which accepts a string and returns a function. When the inner function is invoked it should accept 
a parameter which is a letter, and the inner function should return the number of times that letter appears. This inner function should be 
case insensitive.

counter = letter_counter('Amazing')
counter('a') # 2
counter('m') # 1

counter2 = letter_counter('This Is Really Fun!')
counter2('i') # 2
counter2('t') # 1 
'''

def letter_counter(msg):
    letters = {x: msg.lower().count(x) for x in msg.lower()}
    def inner(cha):
        if cha.lower() in letters: return letters[cha.lower()]
        return 0
    return inner

counter = letter_counter('Amazing')
print(counter('a')) # 2
print(counter('m')) # 1

counter2 = letter_counter('This Is Really Fun!')
print(counter2('i')) # 2
print(counter2('t')) # 1 