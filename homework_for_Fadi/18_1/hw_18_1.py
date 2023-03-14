"""
Task 1
Create a class method named `validate`, which should be called from the `__init__` method to validate parameter email,
passed to the constructor. The logic inside the `validate` method could be to check
if the passed email parameter is a valid email string.

Email validations:
Valid email address format
Email address
(there are links on the website)
"""

print("\nTASk ONE\n")

import re


class Validation:
    def __init__(self, email):
        if self.validate(email):
            self.email = email
        else:
            self.email = None
            print("The email is wrong")

    @classmethod
    def validate(cls, email):
        return re.match(r"^[a-z0-9]+[._-]?[a-z0-9]+[@]\w+[._-]?\w+[.]\w{2,3}$", email)


validation1 = Validation("abc_def@mail.com")
print(validation1.email)

"""
Task 2
Implement 2 classes, the first one is the Boss and the second one is the Worker.

Worker has a property 'boss', and its value must be an instance of Boss.
You can reassign this value, but you should check whether the new value is Boss.
 
Each Boss has a list of his own workers. 
You should implement a method that allows you to add workers to a Boss. 

You're not allowed to add instances of Boss class to workers list directly via access to attribute, 
use getters and setters instead!
You can refactor the existing code.

"""

print("\nTASK TWO\n")


class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []

    def get_workers(self):
        return self.workers

    def set_workers(self, value):
        self.workers = value

    def add_workers(self, workers: list):
        current_workers = self.get_workers()
        current_workers.extend(workers)
        self.set_workers(current_workers)


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self.boss = boss

    def newboss(self, new_boss):
        if isinstance(new_boss, Boss):
            self.boss = new_boss
        else:
            raise TypeError("This is not a real boss!")


prosha = Boss(69, "Prosha", "Pay Geople")
dana = Boss(70, "Dana", "Pay Geople")

misha = Worker(1, "Misha", "Pay Geople", prosha)
sofiia = Worker(2, "Sofiia", "Pay Geople", prosha)
daniil = Worker(3, "Daniil", "Pay Geople", prosha)

daniil.newboss(dana)
print(daniil.boss.name)

dana.add_workers([daniil])
prosha.add_workers([misha, sofiia])

"""
Task 3

Write a class TypeDecorators which has several methods for converting results of functions to a specified type 
(if it's possible):

methods:
to_int
to_str
to_bool
to_float
"""

print("\nTASK THREE\n")


class TypeDecorators:
    @staticmethod
    def to_int(func):
        def wrap(sam_str: str):
            return int(func(sam_str))

        return wrap

    @staticmethod
    def to_str(func):
        def wrap(sam):
            return str(func(sam))

        return wrap

    @staticmethod
    def to_bool(func):
        def wrap(sam):
            return bool(func(sam))

        return wrap

    @staticmethod
    def to_float(func):
        def wrap(sam):
            return float(func(sam))

        return wrap


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_str
def do_str(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


@TypeDecorators.to_float
def do_something_else(string: str):
    return string


assert do_nothing('25') == 25
assert do_something('True') is True
