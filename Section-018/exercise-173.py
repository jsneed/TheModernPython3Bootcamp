# flesh out intersection pleaseeeee
def intersection(list1, list2):
    return list(set(list1) & set(list2))

print(intersection([1, 2, 3], [2, 3, 4]))               # [2, 3]
print(intersection(['a', 'b', 'z'], ['x', 'y', 'z']))   # ['z']
