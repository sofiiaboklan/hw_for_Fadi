"""
Task 1
Write a decorator that prints a function with arguments passed to it.
NOTE! It should print the function, not the result of its execution!

For example:

 "add called with 4, 5"

```

def logger(func):
    pass

@logger
def add(x, y):
    return x + y

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]
"""
print("\nTASK ONE\n")

def logger(func):
    def aaa(*args):
        print(str(func.__name__) + " was called with " + ', '.join(str(e) for e in args))
    return aaa


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


add(2, 3)
square_all(2, 3, 4, 5)

"""
Task 2
Write a decorator that takes a list of stop words and replaces them with * inside the decorated function

def stop_words(words: list):
    pass

@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
"""

print("\nTASK TWO\n")


def stop_words(words: list):
    # words - banned words - ['pepsi', 'BMW']
    def stop_words_1(func):
        # func - create_slogan
        def wrap(*args):
            # args - стрічка, яку треба змінити - drinks pepsi in his brand new BMW!
            func_result = func(*args).split()
            for word in words:
                func_result = [i.replace(word, '*') for i in func_result]

            return ' '.join(func_result)
        return wrap
    return stop_words_1


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


print(create_slogan("Steven"))


assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
assert create_slogan("Sofiia") == "Sofiia drinks * in his brand new *!"

"""
Task 3
Write a decorator `arg_rules` that validates arguments passed to the function.
A decorator should take 3 arguments:

max_length: 15
type_: str
contains: [] - list of symbols that an argument should contain

If some of the rules' checks returns False, the function should return False and print the reason it failed;
otherwise, return the result.


def arg_rules(type_: type, max_length: int, contains: list):
    pass

@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
"""

print("\nTASK THREE\n")


def arg_rules(type_: type, max_length: int, contains: list):
    def arg_rules_1(func):
        def wrap(*args):
            for arg in args:
                if type(arg) != type_:
                    print("The name '" + str(arg) + "' is a different type from " + str(type_))
                    return False

                result = 0
                for rule in contains:
                    if arg.count(rule) > 0:
                        result += 1

                if result != len(contains):
                    print("The name '" + arg + "' doesn't meet the requirements: " + str(contains))
                    return False

                elif len(arg) > max_length:
                    print("The name '" + arg + "' has more symbols than the max_length " + str(max_length))
                    return False

                else:
                    return func(*args)

        return wrap
    return arg_rules_1


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


print(create_slogan("S@SH05"))


assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
assert create_slogan(False) is False
