import sqlite3 as lite
import sys


connection = lite.connect('pets.db')

with connection:

    las = connection.cursor()

    while True:
        id_num = raw_input("Enter ID no. of pet owner, or enter -1 to exit: ")

        if id_num == '-1':
            print 'Exiting Database Query.'
            raise SystemExit

        las.execute("SELECT first_name, last_name, person.age, name, breed,"
                    "pet.age, dead FROM person, pet, person_pet "
                    "WHERE person.id = person_pet.person_id AND "
                    "pet.id = person_pet.pet_id AND person.id=(?)", (id_num))

        person = las.fetchall()

        if len(person) == 0:
            print 'Invalid ID number entered.'
            continue

        for row in person:
            first_name = row[0]
            last_name = row[1]
            age = row[2]
            pet_name = row[3]
            pet_type = row[4]
            pet_age = row[5]
            living = row[6]
            if living == 1:
                print ('{} {}, age {}, owned a {} named {}, '
                       'who was {} years old.').format(first_name, last_name,
                                                       age, pet_type,
                                                       pet_name, pet_age)
            else:
                print ('{} {}, age {}, owns a {} named {}, '
                       'who is {} years old.').format(first_name, last_name,
                                                      age, pet_type,
                                                      pet_name, pet_age)
