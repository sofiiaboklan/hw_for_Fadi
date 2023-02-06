# THEORY ?

print("THEORY ?\n")

# ТУТ РОЗГЛЯДАЄТЬСЯ РОБОТА З ДЕКІЛЬКОМА ФАЙЛАМИ
# ЩЕ Є ФАЙЛИ CARL, OPEN_CARL, CJ, HELLO_AGAIN,USER_INFO, WEEKDAYS

"""

with open('weekdays.txt') as week_file:
    weekdays = [day.rstrip() for day in week_file.readlines()]
print(weekdays)

username = input("Name: ")
with open('user_info.txt', 'w') as file_object:
    file_object.write(username)
    
"""

# LESSON 8
print("\nLESSON 8\n")

# як видалити обʼєкту з дикту: створюєш новий дікт і додаєш те що тобі треба
my_dict = {
    "1": 1,
    "2": 0,
    '3': 3,
    "4": 0,
}

"""
ВАРІАНТ 1

for key, value in my_dict.items():
    if value == 0:
        del my_dict[key]
        my_dict.pop(key)
"""

"""
ВАРІАНТ 2

my_dict_2 = {}

for key, value in my_dict.items():
    if value != 0:
        my_dict_2[key] = value

my_dict = my_dict_2
print(my_dict)
"""

"""
ВАРІАНТ 3

a = "abc"
print(id(a), id(str(a)))

for key, value in dict(my_dict).items():
    if value == 0:
        del my_dict[key]
print(my_dict)
"""

my_dict = {k: v for k, v in my_dict.items() if v != 0}
print(my_dict)

