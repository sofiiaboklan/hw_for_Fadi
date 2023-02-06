"""
Task 1: The greatest number
Write a Python program to get the largest number from a list of random numbers with the length of 10
Constraints: use only while loop and random module to generate numbers
"""

print("TASK ONE\n")

import random

i = 0
lst = []

while i < 10:
    numbers = random.randint(1, 10)
    lst.append(numbers)
    i += 1
lst.sort()
max_ = lst[-1]
print(lst)
print("The largest number is: ", max_)

"""
Task 2: Exclusive common numbers.
Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list containing 
the common integers between the 2 initial lists without any duplicates.
Constraints: use only while loop and random module to generate numbers
"""

print("\nTASK TWO\n")

i = 0
lst_1 = []
lst_2 = []

while i < 10:
    numbers_1 = random.randint(1, 10)
    numbers_2 = random.randint(1, 10)
    lst_1.append(numbers_1)
    lst_2.append(numbers_2)
    i += 1
print("The first list: ", lst_1)
print("The second list: ", lst_2)


def intersection(lst_1, lst_2):
    return list(set(lst_1) & set(lst_2))


print("Their common integers: ", intersection(lst_1, lst_2))

"""
Task 3: Extracting numbers.
Make a list that contains all integers from 1 to 100, then find all integers from the list that are divisible by 7 
but not a multiple of 5, and store them in a separate list. Finally, print the list.
Constraint: use only while loop for iteration
test_list = [round(float(i)) for i in lst]
"""

print("\nTASK THREE\n")

test_list = range(1, 101)
i = 0
result_list = []

while i < 100:
    number1 = test_list[i]
    if number1 % 7 == 0 and number1 % 5 != 0:
        result_list.append(number1)
    i += 1
print(result_list)

