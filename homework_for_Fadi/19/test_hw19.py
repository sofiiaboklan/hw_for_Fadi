"""
Task 1
Pick your solution to one of the exercises in this module.
Design tests for this solution and write tests using unittest library.
"""

print("\nTASK ONE\n")

import json
import unittest
import school


class SchoolTestCase(unittest.TestCase):
    def setUp(self):
        self.sofiia = school.Student("Sofiia", "Boklan", 20, "female")
        self.misha = school.Teacher("Mykhailo", "Stolnikovych", 22, "male", "English", 50000)

    def test_played_hooky(self):
        self.assertEqual(self.sofiia.played_hooky_amount, 0)
        self.sofiia.played_hooky(20)
        self.assertEqual(self.sofiia.played_hooky_amount, 20)

    def test_grade_paper(self):
        self.assertEqual(self.sofiia.grades[self.misha.subject], 0)
        self.misha.grade_paper(self.sofiia, 12)
        self.assertEqual(self.sofiia.grades[self.misha.subject], 12)


"""
Task 2
Write tests for the Phonebook application, which you have implemented in module 1. 
Design tests for this solution and write tests using unittest library
"""

print("\nTASK TWO\n")

import phonebook_app


class PhonebookTestCase(unittest.TestCase):
    def setUp(self):
        self.testPerson = {"first_name": "John",
                      "last_name": "Johnson",
                      "full_name": "John Johnson",
                      "phone_number": "066-876-45-09",
                      "city_or_state": "Florida"}
        self.testPerson2 = {"first_name": "Sofiia",
                           "last_name": "Boklan",
                           "full_name": "Sofiia Boklan",
                           "phone_number": "066-334-35-93",
                           "city_or_state": "Glasgow"}
        try:
            with open("user_info.py") as f:
                self.data = json.load(f)
                self.people = self.data['people']
        except FileNotFoundError:
            raise FileNotFoundError

        with open("phonebook.json", 'w') as f:
            json.dump(self.data, f, indent=2)

    def test_zero(self):
        self.assertEqual(phonebook_app.createNewPerson(self.testPerson), self.testPerson2)

    def test_one(self):
        self.assertEqual(phonebook_app.findPersonByName("John"), self.testPerson)

    def test_two(self):
        self.assertEqual(phonebook_app.findPersonBySurname("Johnson"), self.testPerson)

    def test_three(self):
        self.assertEqual(phonebook_app.findPersonByFullName("John Johnson"), self.testPerson)

    def test_four(self):
        self.assertEqual(phonebook_app.findPersonByNumber("066-876-45-09"), self.testPerson)

    def test_five(self):
        self.assertEqual(phonebook_app.findPersonByCity("Florida"), self.testPerson)

    def test_six(self):
        testPerson2 = self.testPerson
        testPerson2["phone_number"] = "087-456-09-12"
        self.assertEqual(phonebook_app.UpdateNumber(self.testPerson, "087-456-09-12"), testPerson2)

    def test_seven(self):
        self.assertEqual(phonebook_app.DeleteNumber("066-334-35-93"), None)


