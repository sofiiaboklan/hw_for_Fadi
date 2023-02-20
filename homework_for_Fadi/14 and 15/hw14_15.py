"""
Task 1: School

Make a class structure in python representing people at school. Make a base class called Person, a class called Student,
and another one called Teacher. Try to find as many methods and attributes as you can which belong to different classes,
and keep in mind which are common and which are not. For example, the name should be a Person attribute, while salary
should only be available to the teacher.
"""


class Person:
    def __init__(self, firstname: str, surname: str, age: int, sex: str):
        self.firstname = firstname
        self.surname = surname
        self.age = age
        self.sex = sex

    def __str__(self) -> str:
        return f"Hello! My name is {self.firstname} {self.surname}, I am a {self.sex} and I am {self.age} years old."


class Student(Person):
    played_hooky_amount = 0

    def __init__(self, firstname: str, surname: str, age: int, sex: str):
        self.grades = {"English": 0, "Math": 0}
        super().__init__(firstname, surname, age, sex)

    def played_hooky(self, amount: int):
        self.played_hooky_amount += amount


class Teacher(Person):

    def __init__(self, firstname: str, surname: str, age: int, sex: str, subject: str, salary: int):
        self.subject = subject
        self.salary = salary
        super().__init__(firstname, surname, age, sex)

    def grade_paper(self, student: Student, grade: int):
        student.grades[self.subject] = grade


sofiia = Student("Sofiia", "Boklan", 20, "female")
print(sofiia.__str__())
sofiia.played_hooky(20)
print(sofiia.played_hooky_amount)

daniil = Student("Daniil", "Fedorov", 20, "male")
print(daniil.__str__())
daniil.played_hooky(10)
print(daniil.played_hooky_amount)

misha = Teacher("Mykhailo", "Stolnikovych", 22, "male", "English", 50000)
print(misha.__str__())
misha.grade_paper(sofiia, 12)
misha.grade_paper(daniil, 10)

prosha = Teacher("Prokhor", "Mosin", 19, "male", "Math", 20000)
print(prosha.__str__())
prosha.grade_paper(sofiia, 2)
prosha.grade_paper(daniil, 11)

print(sofiia.grades)
print(daniil.grades)

"""
Task 2: Mathematician

Implement a class Mathematician which is a helper class for doing math operations on lists
The class doesn't take any attributes and only has methods:

square_nums (takes a list of integers and returns the list of squares)
remove_positives (takes a list of integers and returns it without positive numbers
filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'
"""


class Mathematician:
    def square_nums(self, nums: list):
        return [i ** 2 for i in nums]

    def remove_positives(self, nums: list):
        for num in nums:
            if num > 0:
                nums.remove(num)
        return nums

    def filter_leaps(self, nums: list):
        new_list = []
        for num in nums:
            if num % 4 == 0:
                new_list.append(num)
        return new_list


m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]

assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]

assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]

"""
Task 3: Product Store

Write a class Product that has three attributes:

type
name
price

Then create a class ProductStore, which will have some Products and will operate with all products in the store. 
All methods, in case they can’t perform its action, should raise ValueError with appropriate error information.

Tips: Use aggregation/composition concepts while implementing the ProductStore class. 
You can also implement additional classes to operate on a certain type of product, etc.
"""


class Product:
    def __init__(self, product_type: str, name: str, price: int):
        self.product_type = product_type
        self.name = name
        self.price = price


class ProductStore:
    prime_price = 1.3

    def __init__(self, stock={}, prices={}, income=0):
        self.stock = stock
        self.prices = prices
        self.income = income

    def add(self, product: Product, amount: int):
        self.stock[product] = amount
        self.prices[product] = product.price * self.prime_price

    def set_discount(self, identifier: str, percent: int, identifier_type: str):
        if identifier_type == "type":
            for key in self.prices.keys():
                if key.product_type == identifier:
                    self.prices[key] *= ((100 - percent) / 100)
        else:
            for key in self.prices.keys():
                if key.name == identifier:
                    self.prices[key] *= ((100 - percent) / 100)

    def sell_product(self, product_name: str, amount: int):
        for key in self.stock.keys():
            if key.name == product_name and self.stock[key] >= amount:
                self.income += amount * self.prices[key]
                self.stock[key] -= amount
                return True
        raise ValueError("Incorrect.")

    def get_income(self):
        return self.income

    def get_all_products(self):
        string = ""
        for key in self.stock.keys():
            newstr = str(key.name) + ": " + str(self.stock[key]) + ", price for one: " + str(self.prices[key]) + "usd"
            string += newstr + "\n"
        return string

    def get_product_info(self, product_name):
        for key in self.stock.keys():
            if key.name == product_name:
                product_tuple = (key.name, self.stock[key])
                return product_tuple


p = Product('Sport', 'Football T-Shirt', 100)

p2 = Product('Food', 'Ramen', 1.5)

s = ProductStore()

s.add(p, 10)

s.add(p2, 300)

print(s.stock, s.prices)

s.set_discount("Sport", 30, "type")
s.set_discount("Ramen", 30, "name")

print(s.prices)

s.sell_product("Football T-Shirt", 2)
print(s.stock)

print(s.get_income())
print(s.get_all_products())

print(s.get_product_info("Ramen"))

# s.sell(‘Ramen’, 10)

# assert s.get_product_info(‘Ramen’) == (‘Ramen’, 290)


"""
Task 4: Custom exception

Create your custom exception named `CustomException`, you can inherit from base Exception class, 
but extend its functionality to log every error message to a file named `logs.txt`. 
Tips: Use __init__ method to extend functionality for saving messages to file
"""


class CustomException(Exception):
    def __init__(self, msg: str):
        with open('logs.txt', 'w') as file_object:
            file_object.write(msg)


def oops():
    raise CustomException("An error lol")


oops()
