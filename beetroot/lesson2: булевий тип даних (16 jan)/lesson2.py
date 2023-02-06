# ТЕОРІЯ 4 ТЕМА
# 16/01/23

# Оператор if

if False:
    print("condition was true")
print("if statement is over")

weather = "cloudy"

if weather == "sunny":
    print("today is a good day")
elif weather == "rainy":
    print("today is a bad day")
else:
    print("today is a lame day")

# and - виграє Фолс
True and True
True
True and False
False
False and False
False

# or - виграє Тру
False or False
False
True or False
True
True or True
True

# not - заперечення
not True
False
not False
True

# дорівнює

6 == 6

6 == 5

# не дорівнює

5 != 6

5 != 5

# більше або менше

5 < 6

5 < 4

5 > 4

5 > 4

# більше менше або дорівнює

5 >= 5

5 >= 4

5 <= 4

# Булеві вирази, None та логічні оператори



# ?

our_condition = 'yes' # assign new value and try to re-run above example

if our_condition == 'yes':
    print('I need to print "yes", because if statement evaluated to True')

# While, break, continue

our_threshold = 5
i = 0
while i < our_threshold:
    print('Do important logic here.')
    i += 1  # воно відображатиметься 5 разів, поки 0 менше або дорівняє 5

i = 10
while i < our_threshold:
    print('Do important logic here.')
    i += 1  # нічого не відображатиметься, бо 10 не менше 5

our_threshold = 10
i = 0

while i < our_threshold:
    print(f'Variable i: {i}.', end=' ')
    print('Do important logic here.')
    i += 1
    if i % 7 == 0:
        print('Good reason to stop')
        break  # воно друкуватиме до 6, коли дійде до 7 то перестане, бо 7 % 7 це 0

our_threshold = 23
i = 1
while i < our_threshold:
    print(f'Variable i: {i}.', end=' ')
    if i % 7 == 0:
        print('Do very very important task and that`s it')
        i += 1
        continue
    print('Do important logic here.')
    i += 1  # поки "і" менше 23 буде лоджік, в той же час коли і буде кратне 7 (%7) воно друкуватиме таск, а контінʼю це типу аби команда використовувалась одночасно


our_threshold = 6  # якщо змінити на "7" то буде виконана "if"
i = 0
while i < our_threshold:
    print(f'Variable i: {i}.', end=' ')
    print('Do important logic here.')
    i += 1
    if i % 7 == 0:
        print('Something went wrong')
        everything_ok = False
        break
else:
    print('This imporatant logic will take place only if nothing broken')

# for-in

a_list  = [1, 2, 3, 4, 5]
i = 0
while i < len(a_list):
    print(a_list[i])
    i += 1  # видасть просто список 1-5, але так типу незручно

for item in a_list:
    print(item) # так легше, бо функція "фор...ін" надає значення айтему а_листа

for ind, item in enumerate(a_list):
    print(ind, item)  # ???

for i in range(len(a_list)):
    print(a_list[i]) # ???

for item in a_list:
    if item == 2:
        break # якщо написати контінʼю то буде список без 2
    print(item)  # буде 1

for item in a_list:
    if item == 10:
        break
    print(item)
else:
    print("ok")




x = 10
if x < 5:
    print(10 + 10)
elif x > 5:
    print(101 - 202)
elif x == 10:
    print(1/0)
else:
    print(1 * 10)

n = 5
while n > 0:
    n -= 1
    if (n % 2) == 0:
        continue
print(n)




# УРОК 2 (16.01)

"""
humor = "humor"
the_name = "the name"
quote = (
    "Sometimes it pays to stay in bed on Monday, rather than spending "
    "the rest of the week debugging Monday\'s code."
)

print(
    f"Code is like {humor}. When you have to explain it, it's bad.",
    f"Experience is %s of everyone {the name} gives to their mistakes.",
    quote,
    sep="\n"
)

print("Let\'s calculate 2 pul two multiplied by 2", 2 + (2 * 2), sep=": ")
c = (2 + 2) * 2  # This is just an example expression

"""

"""
a = input("Input a: ")
if a.isdigit():
    a = int(a)
else:
    print("")

print(repr(a), type(a))
# print(f"You typed {type(a)}")
"""


"""
# bool(): True 1, False 0
# not (по пріоритету нот - енд - ор)
# and *
# or +


1) (not True) or True
2) False or True
== True

not (1) False or (3) True and (2) False
== True
"""

if 1 != 2:
    print("Paradox")
else:
    print("OK")

# = це присвоєння, == це дорівнює, != це не дорівнює

if x < 5:
    print(10 + 10)
elif x > 5 and x != 10:
    print(101-202)
elif x == 10:
    print("1 / 0")
else:
    print (1*10)

"""
це інфа про "is"

user = get_user() -> User, None

# if not user
# if user == None
if user is None:
    print("User not found")


user = get_users() -> [User, ], None

# if not users - список буде пустий, буде фолсом, незрозуміло в чому проблема
if users is None:
    print("Error")
"""

"""
x1 = True
x2 = True

if False and (False or True) and False:

a = False and (1 / 0)
"""

x = input()
y = input()
max_ = ...

if x > y:
    max = x
else:
    max = y

print("X gr" if x > y else "Y is greater")

max = x if x > y else y
