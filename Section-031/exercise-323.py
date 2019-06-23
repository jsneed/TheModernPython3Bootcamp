'''
delete_users("Grace", "Hopper") # Users deleted: 1.
delete_users("Colt", "Steele") # Users deleted: 2.
delete_users("Not", "Here") # Users deleted: 0.
'''

from csv import reader, writer, DictReader, DictWriter

def delete_users(first, last):
    total = 0
    with open('users3.csv', 'r') as file:
        csv_reader = reader(file)
        names = list(csv_reader)

    with open('users3.csv', 'w') as file2:
        csv_writer = writer(file2)
        for user in names:
            if user[0] == first and user[1] == last:
                total += 1
            else:
                csv_writer.writerow([user[0], user[1]])
    return "Users deleted: " + str(total) + "."
    

print(delete_users("Not", "Here"))