'''
triple_and_filter([1,2,3,4]) # [12]
triple_and_filter([6,8,10,12]) # [24,36]
'''

def triple_and_filter(nums):
    return [n *3 for n in nums if n % 4 == 0]

print(triple_and_filter([1,2,3,4]))
print(triple_and_filter([6,8,10,12]))
