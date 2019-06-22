'''
Write a function called double_return which accepts a function and returns another function. 
double_return should decorate a function by returning two copies of the inner function's return value inside of a list.

@double_return 
def add(x, y):
    return x + y
    
add(1, 2) # [3, 3]

@double_return
def greet(name):
    return "Hi, I'm " + name

greet("Colt") # ["Hi, I'm Colt", "Hi, I'm Colt"]
'''

def double_return(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        return [result, result]
    return wrapper

@double_return 
def add(x, y):
    return x + y
    
print(add(1, 2)) # [3, 3]