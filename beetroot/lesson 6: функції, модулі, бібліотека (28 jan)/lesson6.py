# Урок в середу не відбувся, перенесення на суботу (28.01)

# LESSON 6
"""
print("\nLESSON 6\n")

original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
prices = []
for original_price in original_prices:
    if not original_price > 0:
        continue
    prices.append(original_price)
#    prices.append(original_price if original_price > 0 else 0)
#    if original_price > 0:
#        prices.append(original_price)
#    else:
#        prices.append(0)
prices_new = [price for price in original_prices if price > 0]
print(prices_new)


import time
current_time = time.time()
a = []
for i in range(10_000_000):
    a.append(i)
print(f"t={time.time() - current_time:.6f}")

current_time = time.time()
a = [i for i in range(10_000_000)]
print(f"t={time.time() - current_time:.6f}")  # Такий спосіб набагато швидше
"""


# THEORY 8: FUNCTIONS

# 1

def hello_function():
    print("hello from function")
hello_function()

# 2

def favourite_car(car, colour='Black'):
    print("my favourite car is a " + colour + ' ' + car)
favourite_car('Volvo')
favourite_car('Volvo', 'Green')
favourite_car('BMW', 'Blue')

# 3

def increment_values(l):
#    for i in range(len(l)):
#        l[i] += 1
    l = [2, 3, 4]
    print("List inside of function: " + str(l))
original = [1, 2, 3]
increment_values(original)
print("List outside of function: " + str(original))

# 4

length = len("Ukraine")
print(length)

# 5

def sum_of_squares(x, y):
    return_value = x**2 + y**2
    return return_value
print(sum_of_squares(2, 3))

def sum_of_squares(x, y):
    return x**2 + y**2
print(sum_of_squares(2, 3))

def sum_of_squares(*args):
    return_value = 0
    for num in args:
        return_value += num**2
    return return_value
print(sum_of_squares(2, 3, 3, 5, 1, 6))

# 6

def build_pet(species, name, **pet_info):
    pet = {}
    pet['species'] = species
    pet['name'] = name
    for key, value in pet_info.items():
        pet[key] = value
    return pet

my_pet = build_pet('Husky', "Doge", color='White', age=2)
print(my_pet)

# 7

""" A tree of size 3
    *
   ***
  *****
"""

def print_tree(n):
    for i in range(n):
        for j in range(n-i):
            print(' ', end='')
        for k in range(2*i + 1):
            print('*', end='')
        print()

print_tree(7)


# THEORY 9: МОДУЛІ ТА СТАНДАРТНА БІБЛІОТЕКА


