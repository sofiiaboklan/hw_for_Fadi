"""
Task 1
Write a Python program to detect the number of local variables declared in a function.

# NOTES FOR ME (since I obviously got this from some random python forum):
__code__ The code object representing the compiled function body.
co_nlocals is the number of local variables used by the function (including arguments);
"""

print("\nTASK ONE: VERSION ONE\n")


def local_vars():
    a = 1
    b = 2
    c = 3
    d = 4
    print(local_vars.__code__.co_nlocals)


local_vars()

# OR

print("\nTASK ONE: VERSION TWO\n")


def local_vars_1(func):
    print(func.__code__.co_nlocals)


local_vars_1(local_vars)

"""
Task 2
Write a Python program to access a function inside a function (Tips: use function, which returns another function)
"""

print("\nTASK TWO: VERSION ONE\n")


def main_func(a):
    return a * 10 - 10


def func():
    return main_func


y = func()

print("The value of (a * b - 10) is", y(10))

print("\nTASK TWO: VERSION TWO\n")


def func_1(a):
    def func_2(b):
        return a * b - 10

    return func_2


x = func_1(10)
print("The value of (a * b - 10) is", x(50))

"""
Task 3
Write a function called `choose_func` which takes a list of nums and 2 callback functions. 
If all nums inside the list are positive, execute the first function on that list and return the result of it. 
Otherwise, return the result of the second one.
"""

print("\nTASK THREE\n")

nums1 = [1, 2, 3, 4, 5]
nums2 = [-1, -2, 3, -4, 5]


def check(list1, val):
    return all(x > val for x in list1)

# Сорі, я не знаю як зробити цю задачу без цієї додаткової функції, буду вдячна якщо скинете приклад
# (я напевно і так напишу в хоумворк аби мені скинув хтось зі студентів)


def square_nums(nums):
    res = []
    for num in nums:
        res.append(num ** 2)
    return res


def remove_negatives(nums):
    res = []
    for num in nums:
        if num > 0:
            res.append(num)
    return res


def choose_func(nums: list, func1, func2):
    if check(nums, 0):
        return func1(nums)
    else:
        return func2(nums)


print(choose_func(nums1, square_nums, remove_negatives))
print(choose_func(nums2, square_nums, remove_negatives))

# Короче, я впевнена, що зробила задачу не за умовою на багатьох рівнях, але це найкраще до чого я додумалась :(
# І взагалі головне шо вона працює ахахаха
