'''
update_users("Grace", "Hopper", "Hello", "World") # Users updated: 1.
update_users("Colt", "Steele", "Boba", "Fett") # Users updated: 2.
update_users("Not", "Here", "Still not", "Here") # Users updated: 0.
'''

from csv import reader, writer, DictReader, DictWriter

def update_users(old_first, old_last, new_first, new_last):
    total = 0
    with open('users2.csv', 'r') as file:
        csv_reader = reader(file)
        names = list(csv_reader)

    with open('users2.csv', 'w') as file2:
        csv_writer = writer(file2)
        #csv_writer.writerow(["First Name", "Last Name"])
        for user in names:
            if user[0] == old_first and user[1] == old_last:
                csv_writer.writerow([new_first, new_last])
                total += 1
            else:
                csv_writer.writerow([user[0], user[1]])
    return "Users updated: " + str(total) + "."
    
    

print(update_users("Not", "Here", "Still not", "Here"))