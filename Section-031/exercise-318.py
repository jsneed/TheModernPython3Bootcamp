'''
print_users() # None
# prints to the console:
# Colt Steele
'''

from csv import reader, writer, DictReader, DictWriter

def print_users():
    with open('users.csv', 'r') as file:
        csv_reader = reader(file)
        next(csv_reader)
        for user in csv_reader:
            print(user[0] + ' ' + user[1])

print_users()