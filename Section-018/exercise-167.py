'''
list_manipulation([1,2,3], "remove", "end") # 3
list_manipulation([1,2,3], "remove", "beginning") #  1
list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
'''

def list_manipulation(nums, fn, location, value=0):
    if fn == "remove" and location == "end":
        return nums.pop()
    elif fn == "remove" and location == "beginning":
        return nums.pop(0)
    elif fn == "add" and location == "beginning":
        nums.insert(0, value)
        return nums
    elif fn == "add" and location == "end":
        nums.append(value)
        return nums


print(list_manipulation([1,2,3], "remove", "end"))
print(list_manipulation([1,2,3], "remove", "beginning"))
print(list_manipulation([1,2,3], "add", "beginning", 20))
print(list_manipulation([1,2,3], "add", "end", 30))
