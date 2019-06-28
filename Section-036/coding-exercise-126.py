'''
Write a function called two_oldest. The function should take a list of numbers as its argument and return the two highest numbers within 
the list. The returned value should be a list in the format [second oldest age, oldest age].

The order of the numbers passed in could be any order.

two_oldest_ages( [1, 2, 10, 8] ) # [8, 10]
two_oldest_ages( [6,1,9,10,4] ) # [9,10]
two_oldest_ages( [4,25,3,20,19,5] ) # [20,25]
'''

def two_oldest_ages(nums):
    result = []
    result.append(max(nums))
    nums.remove(result[0])
    result.insert(0, max(nums))
    return result


print(two_oldest_ages( [1, 2, 10, 8] )) # [8, 10]
print(two_oldest_ages( [6,1,9,10,4] )) # [9,10]
print(two_oldest_ages( [4,25,3,20,19,5] )) # [20,25]