"""
Task 2: Extend Phonebook application

Functionality of Phonebook application:

Add new entries
Search by first name
Search by last name
Search by full name
Search by telephone number
Search by city or state
Delete a record for a given telephone number
Update a record for a given telephone number
An option to exit the program

The first argument to the application should be the name of the phonebook. 
Application should load JSON data, if it is present in the folder with application, 
else raise an error. After the user exits, all data should be saved to loaded JSON.
"""

import json


def phonebook_application(name_of_phonebook):
    try:
        with open("user_info.py") as f:
            data = json.load(f)
            people = data['people']
    except FileNotFoundError:
        raise FileNotFoundError

    with open(name_of_phonebook + ".json", 'w') as f:
        json.dump(data, f, indent=2)
    while True:
        user_input = input("\nHow can we help you today?\nChoose number from one of these options:\n\n "
                           ">>> 1. Add new entry\n >>> 2. Search by first name\n >>> 3. Search by last name\n "
                           ">>> 4. Search by full name\n >>> 5. Search by the telephone number\n"
                           " >>> 6. Search by city or state\n >>> 7. Delete a record for a given telephone number\n "
                           ">>> 8. Update a record for a given telephone number\n >>> 9. Save and exit\n\n"
                           "Please type in your option here: ")
        if user_input == "1":
            new_person_dict = {}
            test_person = people[0]

            for key in test_person.keys():
                new_person_dict[key] = ""

            user_input_first_name = input("Type in the first name: ")
            user_input_last_name = input("Type in the last name: ")
            user_input_full_name = input("Type in the full name: ")
            user_input_number = input("Type in the phone number: ")
            user_input_city = input("Type in the city or state: ")

            new_person_dict["first_name"] = user_input_first_name
            new_person_dict["last_name"] = user_input_last_name
            new_person_dict["full_name"] = user_input_full_name
            new_person_dict["phone_number"] = user_input_number
            new_person_dict["city_or_state"] = user_input_city

            people.append(new_person_dict)

        elif user_input == "2":
            user_input_name = input("Type in the first name: ")

            for person in people:
                if person["first_name"] == user_input_name:
                    print(person)

        elif user_input == "3":
            user_input_name = input("Type in the last name: ")

            for person in people:
                if person["last_name"] == user_input_name:
                    print(person)

        elif user_input == "4":
            user_input_name = input("Type in the full name: ")

            for person in people:
                if person["full_name"] == user_input_name:
                    print(person)

        elif user_input == "5":
            user_input_number = input("Type in the telephone number: ")

            for person in people:
                if person["phone_number"] == user_input_number:
                    print(person)

        elif user_input == "6":
            user_input_city = input("Type in the city or state: ")

            for person in people:
                if person["phone_number"] == user_input_city:
                    print(person)

        elif user_input == "7":
            user_input_number = input("Type in the telephone number you want to delete: ")

            for person in people:
                if person["phone_number"] == user_input_number:
                    del person['phone_number']
                    print("Success")

        elif user_input == "8":
            user_input_number = input("Type in the telephone number you want to update: ")
            user_input_new_number = input("Type in the new telephone number: ")
            for person in people:
                if person["phone_number"] == user_input_number:
                    person['phone_number'] = user_input_new_number
                    print("Success")

        elif user_input == "9":
            with open(name_of_phonebook + ".json", 'w') as f:
                json.dump(data, f, indent=2)
            print("Thank you! The info was saved. Bye-bye!")
            break

        else:
            print("Please put in a valid option.")


phonebook_application("phonebook")
