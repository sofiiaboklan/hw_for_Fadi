"""
Task 1
Create your own implementation of a built-in function enumerate, named `with_index`,
which takes two parameters: `iterable` and `start`, default is 0. Tips: see the documentation
for the enumerate function.
"""

print("\nTASK ONE\n")


class WithIndex:
    def __init__(self, iterable, start=0):
        self.iterable = iterable
        self.start = start

    def __next__(self):
        if self.start < len(self.iterable):
            output = (self.start, self.iterable[self.start])
            self.start += 1
            return output
        else:
            raise StopIteration

    def __iter__(self):
        return self


my_list = ["prosha", "sofiia", "misha", "daniil"]
print(list(WithIndex(my_list, 2)))

"""
Task 2
Create your own implementation of a built-in function range, named in_range(), which takes three parameters: 
`start`, `end`, and optional step. Tips: See the documentation for `range` function
"""

print("\nTASK TWO\n")

from typing import Optional


class InRange:
    def __init__(self, start, end, step: Optional[int] = 1):
        self.start = start
        self.end = end
        self.step = step

    def __next__(self):
        if self.start < self.end:
            output = self.start
            self.start += self.step
            return output
        else:
            raise StopIteration

    def __iter__(self):
        return self


print(list(InRange(1, 10, 2)))

"""
Task 3
Create your own implementation of an iterable, which could be used inside for-in loop. 
Also, add logic for retrieving elements using square brackets syntax.
"""

print("\nTASK THREE\n")


class MyIterable:
    def __init__(self, elements=None):
        if elements is None:
            elements = []
        self.elements = elements
        self.start = 0

    def __next__(self):
        if self.start < len(self.elements):
            output = self.elements[self.start]
            self.start += 1
            return output
        else:
            raise StopIteration

    def __iter__(self):
        return self


myIterable = MyIterable([[3, 2], 1, 2])
for i in myIterable:
    print(i)
