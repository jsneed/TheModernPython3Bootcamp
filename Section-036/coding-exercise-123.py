'''
Write a function called  sum_up_diagonals  which accepts an NxN list of lists and sums the two main diagonals in the array: the one from 
the upper left to the lower right, and the one from the upper right to the lower left.

EXAMPLES:


list1 = [
  [ 1, 2 ],
  [ 3, 4 ]
]
 
sum_up_diagonals(list1) # 10

list2 = [
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
]
 
sum_up_diagonals(list2) # 30
 
list3 = [
  [ 4, 1, 0 ],
  [ -1, -1, 0],
  [ 0, 0, 9]
]

sum_up_diagonals(list3) # 11

list4 = [
  [ 1, 2, 3, 4 ],
  [ 5, 6, 7, 8 ],
  [ 9, 10, 11, 12 ],
  [ 13, 14, 15, 16 ]
]
 
sum_up_diagonals(list4) # 68
'''

def sum_up_diagonals(matrix):
    matrix_sum = 0
    start = 0
    end = len(matrix) - 1
    i = 0
    while i < len(matrix):
        #print(f"end {end} : start {start} : {matrix[i][start]} : {matrix[i][end]}")
        matrix_sum += matrix[i][start]
        matrix_sum += matrix[i][end]
        start += 1
        end -= 1
        i += 1
    return matrix_sum
    '''
    i = 0
    med = int(len(matrix) / 2)
    print(f"med: {med}")
    while i < len(matrix):
        j = 0
        while j < len(matrix[i]):
            matrix_sum += matrix[i][j]
            j += 1
        i += 1
    return matrix_sum
    '''


list1 = [[ 1, 2 ],[ 3, 4 ]]
print(sum_up_diagonals(list1)) # 10

list2 = [[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]]
print(sum_up_diagonals(list2)) # 30
 
list3 = [[ 4, 1, 0 ],[ -1, -1, 0],[ 0, 0, 9]]
print(sum_up_diagonals(list3)) # 11

list4 = [[ 1, 2, 3, 4 ],[ 5, 6, 7, 8 ],[ 9, 10, 11, 12 ],[ 13, 14, 15, 16 ]]
print(sum_up_diagonals(list4)) # 68