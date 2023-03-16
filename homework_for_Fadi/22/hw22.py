"""
Task 1
Write a program that reads in a sequence of characters and prints them in reverse order,
using your implementation of Stack.
"""
import queue

print("\nTASK ONE\n")

import stack

stack1 = stack.Stack()
word = "Ukraine"

for item in word:
    stack1.push(item)

for _ in range(stack1.size()):
    print(stack1.pop())


"""
Task 2
Write a program that reads in a sequence of characters, and determines whether it's parentheses,
braces, and curly brackets are "balanced."
"""

print("\nTASK TWO\n")

def balanced(string):
    stack2 = stack.Stack()
    for item1 in string:
        if item1 == "[" or item1 == "(" or item1 == "{":
            stack2.push(item1)
        elif item1 == "]":
            if stack2.pop() != "[":
                return False
        elif item1 == ")":
            if stack2.pop() != "(":
                return False
        elif item1 == "}":
            if stack2.pop() != "{":
                return False
    return True


print(balanced("(){}{{{}}[]}"))

"""
Task 3

Extend the Stack to include a method called get_from_stack that searches and returns an element e from a stack.
Any other element must remain on the stack respecting their order. Consider the case in which the element
is not found - raise ValueError with proper info Message
"""

print("\nTASK THREE\n")


class ExtendedStack(stack.Stack):
    def get_from_stack(self, element):
        stack3 = stack.Stack()
        if element in self._items:
            for _ in range(self.size()):
                poppedItem = self.pop()
                if poppedItem != element:
                    stack3.push(poppedItem)
                elif poppedItem == element:
                    for _ in range(stack3.size()):
                        self.push(stack3.pop())
                    return element
        else:
            raise ValueError("This element does not exist!")


extendedStack = ExtendedStack()
extendedStack.push(3)
extendedStack.push(2)
extendedStack.push(1)
extendedStack.push(5)

print(extendedStack.get_from_stack(2))
print(extendedStack)

"""
Task 4
Extend the Queue to include a method called get_from_stack that searches and returns an element e from a queue.
Any other element must remain in the queue respecting their order. Consider the case in which the element
is not found - raise ValueError with proper info Message
"""

print("\nTASK FOUR\n")

import queue


class ExtendedQueue(queue.Queue):
    def get_from_queue(self, element):
        queue1 = queue.Queue()
        if element in self._items:
            for _ in range(self.size()):
                removedItem = self.dequeue()
                if removedItem != element:
                    queue1.enqueue(removedItem)
                elif removedItem == element:
                    for _ in range(self.size()):
                        queue1.enqueue(self.dequeue())
                    for _ in range(queue1.size()):
                        self.enqueue(queue1.dequeue())
                    return element
        else:
            raise ValueError("This element does not exist!")

extendedQueue = ExtendedQueue()

extendedQueue.enqueue(1)
extendedQueue.enqueue(2)
extendedQueue.enqueue(3)
extendedQueue.enqueue(4)

print(extendedQueue.get_from_queue(2))
print(extendedQueue)
