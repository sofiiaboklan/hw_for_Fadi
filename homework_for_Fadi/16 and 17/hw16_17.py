"""
Task 1: Method overloading.

Create a base class named Animal with a method called talk and then create two subclasses:
Dog and Cat, and make their own implementation of the method talk be different.
For instance, Dog’s can be to print ‘woof woof’, while Cat’s can be to print ‘meow’.

Also, create a simple generic function, which takes as input instance of a Cat or Dog classes
and performs talk method on input parameter.
"""

print("\nTASK ONE\n")


class Animal:
    def say_hi(self):
        pass


class Cat(Animal):
    def say_hi(self):
        return 'meow'


class Dog(Animal):
    def say_hi(self):
        return 'woof woof'


def animals_say_hello(animal):
    print(animal.say_hi())


cat = Cat()
dog = Dog()

animals_say_hello(cat)
animals_say_hello(dog)


"""
Task 2: Library

Write a class structure that implements a library. Classes:

1) Library - name, books = [], authors = []
2) Book - name, year, author (author must be an instance of Author class)
3) Author - name, country, birthday, books = []

Library class
Methods:
- new_book(name: str, year: int, author: Author) - returns an instance of Book class and adds the book to the 
books list for the current library.
- group_by_author(author: Author) - returns a list of all books grouped by the specified author
- group_by_year(year: int) - returns a list of all the books grouped by the specified year

All 3 classes must have a readable __repr__ and __str__ methods.

Also, the book class should have a class variable which holds the amount of all existing books
"""

print("\nTASK TWO\n")


class Author:
    def __init__(self, name, country, birthday, books=None):
        if books is None:
            books = []
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = books

    def __str__(self):
        return f"<Name: {self.name}, Country: {self.country}, Birthday: {self.birthday}, Books: {self.books}>"

    def __repr__(self):
        return self.__str__()


class Book:
    amount_of_books = 0

    def __init__(self, name, year, author: Author):
        self.name = name
        self.year = year
        self.author = author
        Book.amount_of_books += 1

    def __str__(self):
        return f"<Name: {self.name}, Year: {self.year}, Author: {self.author}>"

    def __repr__(self):
        return self.__str__()


class Library:
    def __init__(self, name, books=None, authors=None):
        if authors is None:
            authors = []
        if books is None:
            books = []
        self.name = name
        self.books = books
        self.authors = authors

    def __str__(self):
        return f"<Name: {self.name}, Books: {self.books}, Authors: {self.authors}>"

    def __repr__(self):
        return self.__str__()

    def new_book(self, name: str, year: int, author: Author):
        new_book_instance = Book(name, year, author)
        self.books.append(new_book_instance)
        return new_book_instance

    def group_by_author(self, author: Author):
        author_list = []
        for book in self.books:
            if book.author == author:
                author_list.append(book)
        return author_list

    def group_by_year(self, year: int):
        year_list = []
        for book in self.books:
            if book.year == year:
                year_list.append(book)
        return year_list


james = Author("James", "USA", "16.06")

danila = Author("Danila", "Ukraine", "01.01")

book = Book("Book of James", 2000, james)

book1 = Book("Book of James: 2", 2001, james)

book2 = Book("Book of James: 3", 2002, james)

book3 = Book("Book of Danila", 2002, danila)

book4 = Book("Book of Danila: 2", 2003, danila)

library = Library("Library of James", [book, book1, book2, book3, book4], [james, danila])

library.new_book("new book", 2010, danila)

print(library.group_by_author(james))

print(library.group_by_year(2002))

print(book4.amount_of_books)


"""
Task 3: Fraction

Створіть клас Fraction, який буде представляти всю базову арифметичну логіку для дробів (+, -, /, *) з належною 
перевіркою й обробкою помилок. Потрібно додати магічні методи для математичних операцій та операції порівняння між 
об'єктами класу Fraction.


class Fraction:
    pass

if __name__ == "__main__":
    x = Fraction(1, 2) 1/2
    y = Fraction(1, 4) 1/4
    x + y == Fraction(3, 4)
"""

print("\nTASK THREE\n")


class Fraction:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 1/2 + 1/3 -> self + other
    # 2 * 3 = 6 -> nsk -> Fraction( , nsk)
    # 1/2 -> x/6: 6/2 * 1 = 3/6
    # 1/3 -> x/6: 6/3 * 1 = 2/6
    # 3/6 + 2/6 = 5/6

    # 1/2 + 1 =
    # 1 -> Fraction(1, 1)

    def calc_nsk(self, other):
        if other.y == self.y:
            return self.y
        elif (other.y > self.y or self.y > other.y) and other.y % self.y == 0:
            return max(other.y, self.y)
        return other.y * self.y

    def __add__(self, other):
        if isinstance(other, Fraction):
            nsk = self.calc_nsk(other)
            return Fraction(int(other.x * (nsk / other.y) + self.x * (nsk / self.y)), nsk)
        elif isinstance(other, int):
            fraction = Fraction(other, 1)
            return self.__add__(fraction)
        raise TypeError("You can't operate on this type of variable.")

    def __sub__(self, other):
        if isinstance(other, Fraction):
            nsk = self.calc_nsk(other)
            return Fraction(int(self.x * (nsk / self.y) - other.x * (nsk / other.y)), nsk)
        elif isinstance(other, int):
            fraction = Fraction(other, 1)
            return self.__sub__(fraction)
        raise TypeError("You can't operate on this type of variable.")

    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(int(self.x * other.x), (self.y * other.y))
        elif isinstance(other, int):
            fraction = Fraction(other, 1)
            return self.__mul__(fraction)
        raise TypeError("You can't operate on this type of variable.")

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            return Fraction(int(self.x * other.y), (self.y * other.x))
        elif isinstance(other, int):
            fraction = Fraction(other, 1)
            return self.__truediv__(fraction)
        raise TypeError("You can't operate on this type of variable.")

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return other.x == self.x and other.y == self.y
        elif isinstance(other, int):
            fraction = Fraction(other, 1)
            return self.__eq__(fraction)
        raise TypeError("You can't operate on this type of variable.")

    def __ne__(self, other):
        if isinstance(other, Fraction):
            return other.x != self.x or other.y != self.y
        elif isinstance(other, int):
            fraction = Fraction(other, 1)
            return self.__ne__(fraction)
        raise TypeError("You can't operate on this type of variable.")


fraction1 = Fraction(1, 3)
fraction2 = Fraction(1, 4)
result = fraction1 / 5
print(str(result.x) + " / " + str(result.y))


if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    assert x + y == Fraction(3, 4)