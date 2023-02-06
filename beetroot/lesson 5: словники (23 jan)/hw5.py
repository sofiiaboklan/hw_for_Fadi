"""
Task 1
Make a program that has some sentence (a string) on input and returns a dict containing all unique words
as keys and the number of occurrences as values.
"""

print("\nTASK ONE\n")

user = input("Write a sentence and we will give you a dict!: ")

def word_count(str):
    counts = dict()
    words = str.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
print(word_count(user))

"""
Task 2. Input data: (...)
Compute the total price of the stock where the total price is the sum of the price 
of an item multiplied by the quantity of this exact item.
"""

print("\nTASK TWO\n")

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

total_price = {key: stock[key] * prices[key] for key in stock}

print("Total price of our stock is:", sum(total_price.values()))

"""
Task 3: List comprehension exercise.
Use a list comprehension to make a list containing tuples (i, j) where `i` goes from 1 to 10 
and `j` is corresponding to `i` squared.
"""

print("\nTASK THREE\n")

squares = []
for i in range(1, 11):
    for j in ([i**2]):
        squares.append((i, j))
print(squares)

"""
Task 4: 
1) Створити лист із днями тижня.
2) В один рядок (ну або як завжди) створити словник виду: {1: “Monday”, 2:...
3) Також в один рядок або як вдасться створити зворотній словник {“Monday”: 1,


Я спочатку просто вручну це написала, але напевно це занадто просто для домашки, але най буде тут...

week = {
    "Monday": 1,
    "Tuesday": 2,
    "Wednesday": 3,
    "Thursday": 4,
    "Friday": 5,
    "Saturday": 6,
    "Sunday": 7,
}

print(week)
"""

print("\nTASK FOUR\n")

weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
numberOfWeekdays = [1, 2, 3, 4, 5, 6, 7]
week = dict(zip(weekdays, numberOfWeekdays))

print(week)

week_swap = {value: key for key, value in week.items()}
print(week_swap)