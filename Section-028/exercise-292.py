'''
Write a function called delay which accepts a time and returns an inner function that accepts a function. 
When used as a decorator, delay will wait to execute the function being decorated by the amount of time passed into it. 
Before starting the timer, delay will also print a message informing the user that there will be a delay before the decorated function gets run.
(Hint: take a look at the sleep function from the built-in time module if you want to pause code execution for a certain amount of time.)

@delay(3)
def say_hi():
    return "hi"

say_hi()
# should print the message "Waiting 3s before running say_hi" to the console
# should then wait 3 seconds
# finally, should invoke say_hi and return "hi"
'''

from functools import wraps
from time import sleep

def delay(val):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            print(f"Waiting {val}s before running {fn.__name__}")
            sleep(val)
            return fn(*args, **kwargs)
        return wrapper
    return inner

@delay(3)
def say_hi():
    return "hi"

print(say_hi())