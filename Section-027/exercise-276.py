'''
evens = get_multiples(2, 3)
next(evens) # 2
next(evens) # 4
next(evens) # 6
next(evens) # StopIteration

default_multiples = get_multiples()
list(default_multiples) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''

def get_multiples(num=1, count=10):
    total = num
    for i in range(1, count+1):
        yield total
        total += num 

'''
evens = get_multiples(2, 3)
print(next(evens))
print(next(evens))
print(next(evens))
print(next(evens))
'''
default_multiples = get_multiples()
print(next(default_multiples))
print(next(default_multiples))
print(next(default_multiples))
print(next(default_multiples))
print(next(default_multiples))
print(next(default_multiples))
print(next(default_multiples))
print(next(default_multiples))
print(next(default_multiples))
print(next(default_multiples))
print(next(default_multiples))
