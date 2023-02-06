# LESSON 5
# ТЕМА 7

print("\nLESSON 5\nТЕМА 7\n")

# пояснення з юзфул лінкс про суму

a = [
    [1, 2, 3],
    [4, 5, 6],
]

b = sum(a, [])

print(b)

print(sum([1, 2, 3]))  # = 6
print(sum([1, 2, 3], 5))  # = 11

n = [1, 2, 3]
print(sum(n, 5))  # = 11

start = []
for item in a:
    start += item

print(start)

# про set

"""
admin = [...]
moderators = ["moderator1", "moderator2"]
support = ["support_1"]

helpful = None
if len(admin):
    helpful = admin[0]
elif len(moderators):
    helpful = moderators[0]
elif len(support):
    helpful = support[0]

if helpful is None:
    print("Sorry no one is here")
else:
    ...

a = admin or moderators or support
if len(a):
    helpful = a[0]
else:
    print("Sorry no one is here")

a = 2 or 0 or 4
b = 1 and 4 and 0 or 8
print(a, b)
"""




"""
# це все пишеться у консолі

>>> a = {}
...
set()
>>> a.add(3)
>>> a
{3}
>>> b = {2, 3}
>>> a
{3}
>>> b
{2, 3}
>>> a. update(b)
>>> a
{2, 3}

>>> a = {1, 2, 3, 4}
>>> b = {3, 5, 4, 6}
>>> a.union(b)
{1, 2, 3, 4, 5, 6}
>>> a
{1, 2, 3, 4}
>>> b
{3, 4, 5, 6}
>>> a | b
{1, 2, 3, 4, 5, 6}

>>> a.intersection(b)
{3, 4}
>>> a & b
{3, 4}

>>> a and b  # якщо замість "&" використовувати просто "and" воно повертає другий сет і все
{3, 4, 5, 6}
>>> bool(a) and bool(b)
True
>>> bool(a) or bool(b)
True

>>> a.difference(b)
{1, 2}
>>> a - b
{5, 6}
>>> b - a
{5, 6}
>>> a ^ b
{1, 2, 3, 4}
>>> a
{1, 2, 3, 4}
>>> b
{3, 4, 5, 6}

>>> a in b
False
>>> {3, 4} in b
False
>>> {3, 4, 5, 6} in b
True
>>> b - {3, 4}
{5, 6}
>>> {3, 4} - b
set()
>>> len{3, 4} - b
0
>>> len{3, 4, 8} - b
{8}
>>> a.issubset(b)
False
>>> {3.4}.issubset(b)
True
"""


sub = "abc"
string = "a quick broom fox jumps over the lazy dog"

print(string.find(sub))  # виведе -1 бо нема абс в такій послідовності
print(sub in string)  # False
print(set(string).intersection(set(sub)))  # {'a', 'b', 'c'}
print(set(sub).issubset(set(string)))  # True - типу найкращий варіант
print(set(sub).symmetric_difference(set(string)))

# словники

price_list = {
    "apple": 9.99,
    "orange": 14.99,
    "cherry": 26.25,
}

# w.get("apple")
# w["apple"]
# w.pop("apple")
# w.setdefault("apple")

cart = {}
# cart["apple"] = 1
cart["orange"] = 0
cart["cherry"] = 0

print(cart)

# if "apple" in cart.keys():
#     cart["apple"] += 1
# else:
#     cart["apple"] = 1

# print(cart)

if "apple" not in cart.keys():
    cart["apple"] = 0

cart["apple"] += 1
print(cart)

print("#" * 30)

cart = {key: value for key, value in cart.items() if value != 0}

# for key, value in cart.items():
#    if value == 0:
#        del cart[key]

print(cart)



