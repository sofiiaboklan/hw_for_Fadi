# 14/01/23

glass = "water"
cup = "tea"

glass, cup = cup, glass  #аби поміняти змінні

bottle = glass  # "water"
glass = cup  # "tea"
cup = bottle  # "water"

tmp1 = glass
tmp2 = cup
cup = tmp1
glass = tmp2

# пайтон сам змінює наші змінні (кап глес) на тмп1 тмп2

socket = ...
print(type(socket))
print(dir("asd"))

# задачка, шукаємо гіпотенузу
a = 4
b = 16
c = (a ** 2 + b ** 2) ** 0.5

print(f"C = {round (c,5)}")
print(f"C = {c:.5f}")

row = "| {var} | {value:>5.2f} |"
print("-" * 12)
print(row.format (
    var="a",
    value=a
))

print(row.format (
    var="b",
    value=c
))

print(row.format (
    var="c",
    value=c
))

""""
-------
| a | 0000 |
| b | 0000 |
| c | 0000 |

"""

