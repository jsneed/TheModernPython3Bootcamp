'''
This is another trickier exercise.  Don't feel bad if you get stuck or need to move on and come back later on!

Write a function called mode. This function accepts a list of numbers and returns the most frequent number in the list of numbers. 
You can assume that the mode will be unique.

mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]) # 4
'''

# define mode below:
def mode(nums):
    freq = {num: nums.count(num) for num in nums}
    freq_max = max(freq.values())
    temp = [k for k,v in freq.items() if v == freq_max]
    return temp[0]

print(mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4,8])) # 4
