"""
Task 1: A simple function.
Create a simple function called favorite_movie, which takes a string containing
the name of your favorite movie. The function should then print “My favorite movie is named {name}”.
"""
print("\nTASK ONE: version one.\n")


def favorite_movie():
    movie_name = input("What is your favorite movie?: ")
    print(f"My favourite movie is {movie_name}.")


favorite_movie()

# OR

print("\nTASK ONE: version two.\n")


def favorite_movie_1():
    movie_name = "Baby Driver"
    print(f"My favourite movie is {movie_name}.")


favorite_movie_1()

"""
Task 2: Creating a dictionary.
Create a function called make_country, which takes in a country’s name and capital 
as parameters. Then create a dictionary from those two, with ‘name’ as a key and ‘capital’ as a parameter. 
Make the function print out the values of the dictionary to make sure that it works as intended.
"""

print("\nTASK TWO\n")


def make_country():
    country_name = "Ukraine, Italy, Poland"
    country_capital = "Kyiv, Rome, Warsaw"
    keys = country_name.split(',')
    values = country_capital.split(',')
    output_dict = dict(zip(keys, values))
    print(output_dict)
    print(output_dict.values())


make_country()

"""
Task 3: A simple calculator.
Create a function called make_operation, which takes in a simple arithmetic operator 
as a first parameter (to keep things simple let it only be ‘+’, ‘-’ or ‘*’) and an arbitrary number of arguments 
(only numbers) as the second parameter. Then return the sum or product of all the numbers in the arbitrary parameter. 
For example:

the call make_operation(‘+’, 7, 7, 2) should return 16
the call make_operation(‘-’, 5, 5, -10, -20) should return 30
the call make_operation(‘*’, 7, 6) should return 42  
"""

print("\nTASK THREE\n")

import operator


def make_function(operator, number1, *numbers):
    if operator == '+':
        result = number1
        for key in numbers:
            result += key
        return result
    elif operator == '-':
        result = number1
        for key in numbers:
            result -= key
        return result
    else:
        result = number1
        for key in numbers:
            result *= key
        return result


print(make_function('+', 100, 1, 125))
