'''
Write a function called find_greater_numbers which accepts a list and returns the number of times a number is followed by a larger 
number across the entire list.

Take the example find_greater_numbers([6,1,2,7]) # 4 , there are 4 times where a number is followed by a greater number:

2 > 1
7 > 6
7 > 1
7 > 2

find_greater_numbers([1,2,3]) # 3 
find_greater_numbers([6,1,2,7]) # 4
find_greater_numbers([5,4,3,2,1]) # 0
find_greater_numbers([]) # 0
'''

def find_greater_numbers(nums):
    counter = 0
    for i, num in enumerate(nums):
        for j, num2 in enumerate(nums[i:]):
            if num2 > num:
                counter += 1
    return counter

print(find_greater_numbers([1,2,3]))        # 3 
print(find_greater_numbers([6,1,2,7]))      # 4
print(find_greater_numbers([5,4,3,2,1]))    # 0
print(find_greater_numbers([]))             # 0