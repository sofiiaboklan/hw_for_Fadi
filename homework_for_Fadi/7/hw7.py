"""
Task 1
Write a function called oops that explicitly raises an IndexError exception when called.
Then write another function that calls oops inside a try/except statement to catch the error.
What happens if you change oops to raise KeyError instead of IndexError?
"""

print("\nTASK ONE\n")


def oops():
    raise IndexError


def oops_1():
    try:
        oops()
    except IndexError:
        print('You have caught the Index Error.')


oops_1()

# If I change oops()'s exception to KeyError, it will raise a KeyError in oops_1()
# and we will not see the message in the last exception 'You have caught the Index Error.'

"""
Task 2
Write a function that takes in two numbers from the user via input(), call the numbers a and b
a) and then returns the value of squared a divided by b, 
b) construct a try-except block which raises an exception if the two values given by the input function were not numbers, 
c) and if value b was zero (cannot divide by zero).    
"""

print("\nTASK TWO\n")


def user_numbers():
    while True:
        try:
            a = int(input(">>> "))
            b = int(input(">>> "))
            print(f"{a}^2 / {b} = {a ** 2 / b}")
            break
        except ValueError:
            print("That wasn't a number, try again.")
        except ZeroDivisionError:
            print("You can't divide by zero, try again.")


user_numbers()
