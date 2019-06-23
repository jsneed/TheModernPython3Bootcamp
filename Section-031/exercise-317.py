'''
add_user("Dwayne", "Johnson") # None
# CSV now has two data rows:

# First Name,Last Name
# Colt,Steele
# Dwayne,Johnson
'''
from csv import reader, writer, DictReader, DictWriter

def add_user(first, last):
    with open('users.csv', 'a') as file:
        csv_writer = writer(file)
        csv_writer.writerow([first, last])

add_user("Dwayne", "Johnson") 
