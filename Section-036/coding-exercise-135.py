'''
Generator Exercise

Write a function called next_prime, which returns a generator that will yield an unlimited number of primes, starting from the first 
prime (2).

Recall that a prime number is any whole number that has exactly two divisors: one and the number itself. The first few 
primes are 2, 3, 5, 7, 11, ... .

primes = next_prime()
[next(primes) for i in range(25)]
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
'''

def next_prime():
    prime = 1
    while True:
        prime += 1
        divisors = []
        for j in range(1, prime+1):
            if prime % j == 0:
                divisors.append(j)
        if len(divisors) == 2:
            yield prime

primes = next_prime()
print([next(primes) for i in range(25)])
