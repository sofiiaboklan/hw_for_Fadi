# INPUT ТА ШВИДКИЙ ОГЛЯД ІМПОРТІВ
# 18/01/23
# конспект з теорії

"""
input("Give me smt: ")

# ПИСАТИ ТРЕБА В КОНСОЛІ !!!

value = input("Please enter a string:\n")

print(f'You entered {value} and its type is {type(value)}')

value = input("Please enter an integer:\n")  # integer is a number

print(f'You entered {value} and its type is {type(value)}')
"""

# гра камінь ножиці папір

"""
user_name = (input("Please insert name: "))
print("Greetings, " + str(user_name))

import random
print("Let's play rock, paper, scissors")
player = input("Choose rock, paper, scissors by typing r, p or s: ")

if player == "r" or player == "p" or player == "s":
    computer = random.randint(1, 3)
    # 1 == r
    # 2 == p
    # 3 == s
    if (computer == 1 and player == 'r' or computer == 2 and player == "p" or
        computer == 3 and player == "s"):
        print("It is a draw")
    elif (computer == 1 and player == "p" or computer == 2 and player == "s" or
          computer == 3 and player == "r"):
          print("Congratulations, you won!")
    else:
        print("You lost!")
else:
    print("Your input was in the format, no game for you")
"""

# !!! ще треба почитати і дописати про імпорт




# LESSON 3

"""
a = 'a' + 'x' if '123'.isdigit() else 'y' + 'b'
a = 'a' + 'x' if True _____ else 'y' + 'b'
іф це умова, а не просто продовження коду
тобто задачка була: додай а+х, якщо 123 це цифри, якщо це не цифри то додай у+б
"""

"""
a = 5
while a >= 0:
    print(a)
    a -= 1  # друкуватиметься список від 5 до 0
print(a)  # а буде дорівнювати -1 після такого списку
"""


"""
Таск 1
За допомогою циклу while, написати програму, що знаходить факторіал числа N.
Програма повинна починатися з рядка:
n = ...  # n is unsigned positive integer (n > 0)
"""

"""
while True:
    n = input("Enter your number: \n")
    if n == "quit":
        break
    if not n.isdigit():
        print("Use numbers only")

    n = int(n)
    n_fact = 1
    a = 1

    while a != n:
        a += 1
        n_fact *= a

    print(n_fact)
"""

"""
Користувач вводе з клавіатури три цілих числа N, A і B.
Програма шукає всі цілі числа в діапозоні [0 .. N] і виводить:
"Число <number> кратне A!", ящо число діляться на A без залишку;
"Число <number> кратне B!", ящо число діляться на B без залишку.
Якщо число діляться без залишку як на A, так і на B, програма виводить "Бінго! Число <number> ділеться як на A, 
так і на B!" і завершує роботу.
"""
"""
while True:
    N = input("Enter N:")
    A = input("Enter A:")
    B = input("Enter B:")

    if N == "quit" or A == "quit" or B == "quit":
        break

    if not N.isdigit() or not A.isdigit() or not B.isdigit():
        print("Use numbers only!")
        continue

    N, A, B = int(N), int(A), int(B)

    number = 1

    while number != N:
        if number % A == 0 and number % B == 0:
            print(f"Бінго! Число {number} ділиться як на A, так і на B!")
            break
        elif number % A == 0:
            print (f"Число {number} кратне A!")
        elif number % B == 0:
            print(f"Число {number} кратне B!")

        number += 1
"""
"""
# вирішення викладача першої задачи

a = int(input("a:"))
fact = 1

while a > 0:
    fact *= a
    a -= 1

print(a)
"""
"""
a = int(input("a: "))

while a > 0:
    a -= 1
    if a % 2 == 0:
        continue
    else:
        print("else")
"""

