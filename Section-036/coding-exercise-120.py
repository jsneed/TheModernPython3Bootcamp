'''
same_frequency(551122,221515) # True
same_frequency(321142,3212215) # False
same_frequency(1212, 2211) # True
'''

def same_frequency(num1, num2):
    nums = "0123456789"
    str1 = str(num1)
    str2 = str(num2)
    digits1 = {x : str1.count(x) for x in nums}
    digits2 = {x : str2.count(x) for x in nums}
    #print(digits1)
    #print(digits2)
    return digits1 == digits2
    

print(same_frequency(551122,221515)) # True
print(same_frequency(321142,3212215)) # False
print(same_frequency(1212, 2211)) # True