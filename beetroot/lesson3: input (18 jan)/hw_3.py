"""
Task 1: The Guessing Game.
Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated.
The result should be sent back to the user via a print statement.
"""

print("TASK ONE\n")

user_name = (input("Please insert name: "))
print("\nGreetings, " + str(user_name))

import random
print("\nGuess which number I am thinking about!")

computer = random.randint(1, 10)

while True:
    player = input("\nChoose a number from 1 to 10: ")
    if int(player) == computer:
        print(f"\nYay! You win! I also guessed {player}!")
        break
    print("\nOh no! You lost! Try again")

"""
Task 2: The birthday greeting program.
Write a program that takes your name as input, and then your age as input and greets you with the following:
“Hello <name>, on your next birthday you’ll be <age+1> years”
"""

print("\nTASK TWO\n")

user_name = (input("What is your name?: "))
user_age = int(input("\nHow old are you?: "))
num1 = 1

while int(user_age):
    print(f"\nHello {user_name}, on your next birthday you’ll be {user_age + num1} years old!")
    break


"""
Task 3: Words combination
Create a program that reads an input string and then creates and prints
5 random strings from characters of the input string.
For example, the program obtained the word ‘hello’, so it
should print 5 random strings(words) that combine characters

'h', 'e', 'l', 'l', 'o' -> 'hlelo', 'olelh', 'loleh' …

Tips: Use random module to get random char from string)
"""

print("\nTASK THREE\n")

word = input("Put in a word and we will give you 5 random strings out of it: ")
rand_word_1 = ''.join(random.sample(word, len(word)))
rand_word_2 = ''.join(random.sample(word, len(word)))
rand_word_3 = ''.join(random.sample(word, len(word)))
rand_word_4 = ''.join(random.sample(word, len(word)))
rand_word_5 = ''.join(random.sample(word, len(word)))
num = 1
while num > 0:
    print(rand_word_1, rand_word_2, rand_word_3, rand_word_4, rand_word_5)
    num -= 1

"""
Task Four: від викладача
Користувач вводе з клавіатури три цілих числа N, A і B.
Програма шукає всі цілі числа в діапозоні [0 .. N] і виводить:
"Число <number> кратне A!", ящо число діляться на A без залишку;
"Число <number> кратне B!", ящо число діляться на B без залишку.
Якщо число діляться без залишку як на A, так і на B, програма виводить "Бінго! Число <number> ділеться як на A, 
так і на B!" і завершує роботу.
"""
print("\nTASK FOUR\n")

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
            print(f"Число {number} кратне A!")
        elif number % B == 0:
            print(f"Число {number} кратне B!")

        number += 1
