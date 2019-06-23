'''
find_user("Colt", "Steele") # 1
find_user("Alan", "Turing") # 3
find_user("Not", "Here") # 'Not Here not found.'
'''

from csv import reader, writer, DictReader, DictWriter

def find_user(first, last):
    with open('users.csv', 'r') as file:
        csv_reader = list(reader(file))
        i = 0
        while i < len(csv_reader):
            # for (index, row) in enumerate(csv_reader):
            if csv_reader[i][0] == first and csv_reader[i][1] == last:
                return i
            i += 1
    return 'Not Here not found.'

print(find_user("Colt", "Steele"))


