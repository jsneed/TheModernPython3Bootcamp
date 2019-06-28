'''
remove_every_other([1,2,3,4,5]) # [1,3,5] 
remove_every_other([5,1,2,4,1]) # [5,2,1]
remove_every_other([1]) # [1] 
'''

def remove_every_other(input):
    result = []
    insert = True
    for i in input:
        if insert:
            result.append(i)
            insert = False
        else:
            insert = True
    return result


print(remove_every_other([1,2,3,4,5])) # [1,3,5] 
print(remove_every_other([5,1,2,4,1])) # [5,2,1]
print(remove_every_other([1])) # [1] 