'''
Write a function called three_odd_numbers, which accepts a list of numbers and returns True  if any three consecutive numbers sum to an 
odd number.

three_odd_numbers([1,2,3,4,5]) # True
three_odd_numbers([0,-2,4,1,9,12,4,1,0]) # True
three_odd_numbers([5,2,1]) # False
three_odd_numbers([1,2,3,3,2]) # False
'''

def three_odd_numbers(nums):
    if len(nums) < 3: return False
    for i, num in enumerate(nums[0:-2]):
        if (num + nums[i+1] + nums[i+2]) %2 != 0:
            return True
    return False

print(three_odd_numbers([1,2,3,4,5])) # True
print(three_odd_numbers([0,-2,4,1,9,12,4,1,0])) # True
print(three_odd_numbers([5,2,1])) # False
print(three_odd_numbers([1,2,3,3,2])) # False