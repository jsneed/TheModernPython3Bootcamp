def remove_negatives(nums):
    positives = list(filter(lambda n: n >= 0, nums))
    return positives

print(remove_negatives([3, 7, 9, -2, 4, -11, 0, -227]))
