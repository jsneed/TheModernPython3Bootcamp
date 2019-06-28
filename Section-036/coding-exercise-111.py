'''
Write a function called sum_pairs which accepts a list and a number and returns the first pair of numbers that sum to the number passed 
to the function.

sum_pairs([4,2,10,5,1], 6) # [4,2]
sum_pairs([11,20,4,2,1,5], 100) # []
'''

def sum_pairs(nums, sum):
    result = []
    for (i, x) in enumerate(nums):
        for (j, y) in enumerate(nums):
            if i == j:
                break
            elif sum == x + y:
                result.append(y)
                result.append(x)
                return result
    return result

print(sum_pairs([4,2,10,5,1], 6)) # [4,2]
print(sum_pairs([11,20,4,2,1,5], 100)) # []