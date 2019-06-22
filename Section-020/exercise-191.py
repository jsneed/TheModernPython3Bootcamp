# Implement your is_all_strings function below:
def is_all_strings(strs):
    #temp = [s for s in strs if type(s) == str]
    #print(temp)
    #return all(s for s in strs if type(s) == 'str')
    #return not any(s for s in strs if type(s) == str)

    return all(type(l) == str for l in strs)
    #return all([type(l) == str for l in strs])


print(is_all_strings(['dffsdfs', 'fdfsf', 44, 9.7]))
print(is_all_strings(['dffsdfs', 'fdfsf']))
