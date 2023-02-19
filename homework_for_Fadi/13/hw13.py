"""
Task 1: A Person class

Make a class called Person. Make the __init__() method take firstname, lastname, and age as parameters
and add them as attributes. Make another method called talk() which makes prints a greeting from the person containing,
for example like this: “Hello, my name is Carl Johnson and I’m 26 years old”.
"""

print("\nTASK ONE\n")


class Person:

    def __init__(self, firstname: str, surname: str, age: int):
        self.firstname = firstname
        self.surname = surname
        self.age = age

    def talk(self):
        print(f"Hello, my name is {self.firstname} {self.surname} and I'm {self.age} years old!")


if __name__ == "__main__":
    sofiia = Person("Sofiia", "Boklan", "20")
    sofiia.talk()

"""
Task 2: Doggy age

Create a class Dog with class attribute `age_factor` equals to 7. Make __init__() which takes values for a dog’s age. 
Then create a method `human_age` which returns the dog’s age in human equivalent.
"""

print("\nTASK TWO\n")


class Dog:
    age_factor = 7

    def __init__(self, age: int):
        self.age = age

    def human_age(self):
        return self.age * self.age_factor


if __name__ == "__main__":
    dog = Dog(5)
    print(dog.human_age())

"""
Task 3: TV controller

Create a simple prototype of a TV controller in Python. It’ll use the following commands:

first_channel() - turns on the first channel from the list.
last_channel() - turns on the last channel from the list.
turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
current_channel_attr() - returns the name of the current channel.

is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or 
'name' exists in the list, or "No" - in the other case.
 
The default channel turned on before all commands is №1.
Your task is to create the TVController class and methods described above.
"""

CHANNELS = ["BBC", "Discovery", "TV1000"]


class TVController:
    current_channel_attr = 1

    def __init__(self, channels: list):
        self.channels = channels

    def first_channel(self):
        self.current_channel_attr = 1
        return self.channels[self.current_channel_attr - 1]

    def last_channel(self):
        self.current_channel_attr = len(self.channels)
        return self.channels[self.current_channel_attr - 1]

    def turn_channel(self, n: int):
        self.current_channel_attr = n
        return self.channels[self.current_channel_attr - 1]

    def next_channel(self):
        if self.current_channel_attr == len(self.channels):
            self.current_channel_attr = 1
        else:
            self.current_channel_attr += 1
        return self.channels[self.current_channel_attr - 1]

    def previous_channel(self):
        if self.current_channel_attr == 1:
            self.current_channel_attr = len(self.channels)
        else:
            self.current_channel_attr -= 1
        return self.channels[self.current_channel_attr - 1]

    def current_channel(self):
        return self.channels[self.current_channel_attr]

    def is_exist(self, n: int or str):
        if type(n) is int and n > len(self.channels) or type(n) is str and self.channels.count(n) == 0:
            return "No"
        else:
            return "Yes"


controller = TVController(CHANNELS)

assert controller.first_channel() == "BBC"

assert controller.last_channel() == "TV1000"

assert controller.turn_channel(1) == "BBC"

assert controller.next_channel() == "Discovery"

assert controller.previous_channel() == "BBC"

assert controller.current_channel() == "Discovery"

assert controller.is_exist(4) == "No"

assert controller.is_exist("BBC") == "Yes"
