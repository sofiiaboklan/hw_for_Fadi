import json

name_of_phonebook = "phonebook"

try:
    with open("user_info.py") as f:
        data = json.load(f)
        people = data['people']
except FileNotFoundError:
    raise FileNotFoundError

with open(name_of_phonebook + ".json", 'w') as f:
    json.dump(data, f, indent=2)


def createNewPerson(test_person):
    new_person_dict = {}

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

    return new_person_dict


def findPersonByName(name):
    for person in people:
        if person["first_name"] == name:
            return person


def findPersonBySurname(name):
    for person in people:
        if person["last_name"] == name:
            return person


def findPersonByFullName(name):
    for person in people:
        if person["full_name"] == name:
            return person


def findPersonByNumber(number):
    for person in people:
        if person["phone_number"] == number:
            return person


def findPersonByCity(city_or_state):
    for person in people:
        if person["city_or_state"] == city_or_state:
            return person


def DeleteNumber(number):
    for person in people:
        if person["phone_number"] == number:
            del person['phone_number']
            return None


def UpdateNumber(person, new_number):
    person['phone_number'] = new_number
    return person


def phonebook_application(name_of_phonebook):
    # while True:
    user_input = input("\nHow can we help you today?\nChoose number from one of these options:\n\n "
                           ">>> 1. Add new entry\n >>> 2. Search by first name\n >>> 3. Search by last name\n "
                           ">>> 4. Search by full name\n >>> 5. Search by the telephone number\n"
                           " >>> 6. Search by city or state\n >>> 7. Delete a record for a given telephone number\n "
                           ">>> 8. Update a record for a given telephone number\n >>> 9. Save and exit\n\n"
                           "Please type in your option here: ")
    if user_input == "1":

        test_person = people[0]

        people.append(createNewPerson(test_person))

    elif user_input == "2":
        user_input_name = input("Type in the first name: ")
        print(findPersonByName(user_input_name))

    elif user_input == "3":
        user_input_name = input("Type in the last name: ")
        print(findPersonBySurname(user_input_name))

    elif user_input == "4":
        user_input_name = input("Type in the full name: ")
        print(findPersonByFullName(user_input_name))

    elif user_input == "5":
        user_input_number = input("Type in the telephone number: ")
        print(findPersonByNumber(user_input_number))

    elif user_input == "6":
        user_input_city = input("Type in the city or state: ")
        print(findPersonByCity(user_input_city))


    elif user_input == "7":
        user_input_number = input("Type in the telephone number you want to delete: ")
        DeleteNumber(user_input_number)
        print("Success! Number deleted.")


    elif user_input == "8":
        user_input_number = input("Type in the telephone number you want to update: ")
        user_input_new_number = input("Type in the new telephone number: ")
        for person in people:
            if person['phone_number'] == user_input_number:
                print(UpdateNumber(person, user_input_new_number))
                continue


    elif user_input == "9":
        with open(name_of_phonebook + ".json", 'w') as f:
            json.dump(data, f, indent=2)
        print("Thank you! The info was saved. Bye-bye!")

    else:
        print("Please put in a valid option.")


phonebook_application(name_of_phonebook)
