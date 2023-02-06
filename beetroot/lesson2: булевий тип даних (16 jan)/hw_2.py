"""
Task 1: String manipulation

Write a Python program to get a string made of the first 2 and the last 2 chars from a given string.
If the string length is less than 2, return instead of the empty string.

Sample String: 'helloworld'

Expected Result : 'held'

Sample String: 'my'

Expected Result : 'mymy'

Sample String: 'x'

Expected Result: Empty String

Tips:
Use built-in function len() on an input string
Use positive indexing to get the first characters of a string and negative indexing to get the last characters
"""

print("TASK ONE\n")

def string_both_ends(str):
  if len(str) < 2:
    return ''

  return str[0:2] + str[-2:]

print(string_both_ends("helloworld"))
print(string_both_ends("my"))
print(string_both_ends("x"))

"""
Task 2: The valid phone number program.

Make a program that checks if a string is in the right format for a phone number. 
The program should check that the string contains only numerical characters and is only 10 characters long. 
Print a suitable message depending on the outcome of the string evaluation.
"""

print("\nTASK TWO\n")
phone_number = (input("Please type in your phone number: "))
while len(phone_number) != 10 or not phone_number.isdigit():
    print("You have not entered a 10 digit value! Please try again.")
    phone_number = input("Please type in your phone number: ")
print("Thank you!")

"""
Task 3: The math quiz program.

Write a program that asks the answer for a mathematical expression, checks whether the user is right or wrong, 
and then responds with a message accordingly.
"""

print("\nTASK THREE\n")

the_answer = (input("What is 2+4(3+6)?: "))
while the_answer != "38":
    print("Incorrect! Try again!")
    the_answer = (input("What is 2+4(3+6)?: "))
print("Yay! It's correct.")


"""
Task 4: The name check.

Write a program that has a variable with your name stored (in lowercase) and then asks for your name as input. 
The program should check if your input is equal to the stored name even if the given name has another case, e.g., 
if your input is “Anton” and the stored name is “anton”, it should return True.
"""

print("\nTASK FOUR\n")

my_name = "sofia"
your_name = (input("What is your name?: "))
while your_name != my_name:
    if your_name[0] == my_name.upper()[0]:
        break
    print("That is not your name")
    your_name = input("What is your name?: ")
print("Thank you!")

"""
Task 5
Дана змінна month, яка може приймати будь-яке значення.
Необхідно написати програму, яка виведе строку "Ви народились <сезон>", в залежності від номеру місяця.
Програма повинна починатися з рядка (можна використати функцію input()):
month = ...  # Any value
"""

print("\nTASK FIVE\n")

month = input("Please insert a number of the month you were born in: ")
if month == "12" or month == "1" or month == "2":
    print("You were born in winter!")
elif month == "3" or month == "4" or month == "5":
    print("You were born in spring!")
elif month == "6" or month == "7" or month == "8":
    print("You were born in summer!")
elif month == "9" or month == "10" or month == "11":
    print("You were born in autumn!")
else:
    print("Please insert a correct number:(")
