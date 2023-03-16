"""
Task 1: Extend UnorderedList.
Implement append, index, pop, insert methods for UnorderedList.

Also implement a slice method, which will take two parameters `start` and `stop`, and return a copy of the list
starting at the position and going up to but not including the stop position.
"""

print("\nTASK ONE\n")

import unordered
import node


class ExtendedUnorderedList(unordered.UnorderedList):
    def append(self, element):
        if self._head is None:
            self._head = node.Node(element)
            return True
        current_node = self._head
        while current_node.get_next() is not None:
            current_node = current_node.get_next()
        current_node.set_next(node.Node(element))

    def index(self, element):
        counter = 0
        current_node = self._head
        try:
            while current_node.get_data() != element:
                current_node = current_node.get_next()
                counter += 1
        except AttributeError:
            raise AttributeError("This value does not exist in this list")
        return counter

    def pop(self):
        current_node = self._head
        if current_node is None:
            raise AttributeError("This list is empty")
        self._head = current_node.get_next()
        return current_node

    def insert(self, element, index):
        element = node.Node(element)
        current_node = self._head
        if index == 0:
            element.set_next(self._head)
            self._head = element
            return True
        for _ in range(index - 1):
            if current_node.get_next() is None:
                current_node.set_next(element)
                return True
            current_node = current_node.get_next()
        element.set_next(current_node.get_next())
        current_node.set_next(element)
        return True

    def slice(self, start, stop):
        if stop > self.size():
            raise AttributeError("The list is smaller than -stop- index")
        list = ExtendedUnorderedList()
        current_node = self._head
        for _ in range(start):
            current_node = current_node.get_next()
        for _ in range(stop - 1):
            list.append(current_node.get_data())
            current_node = current_node.get_next()

        return list



unorderedlist = ExtendedUnorderedList()
unorderedlist.add(1)
unorderedlist.add(2)
unorderedlist.add(3)
unorderedlist.append(4)
print(unorderedlist)
print(unorderedlist.index(4))
print(unorderedlist.pop().get_data())
print(unorderedlist)
unorderedlist.insert(9, 5)
print(unorderedlist)
print(unorderedlist.slice(1, 3))


"""
Task 2
Implement a stack using a singly linked list.
"""

print("\nTASK TWO\n")

class Stack:
    def __init__(self):
        self.items = ExtendedUnorderedList()
        self._head = None

    def is_empty(self):
        return self.items.is_empty()

    def push(self, item):
        self.items.add(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items._head

    def size(self):
        return self.items.size()

    def __repr__(self):
        representation = "<UnorderedList: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + ">"

    def __str__(self):
        return self.__repr__()


my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
print(my_stack.pop().get_data())
print(my_stack.peek().get_data())
print(my_stack.size())


"""
Task 3
Implement a queue using a singly linked list.
"""


print("\nTASK THREE\n")


class Queue:

    def __init__(self):
        self.items = ExtendedUnorderedList()
        self._head = None

    def is_empty(self):
        return self.items.is_empty()

    def enqueue(self, item):
        self.items.add(item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return self.items.size()

    def __repr__(self):
        representation = "<UnorderedList: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + ">"

    def __str__(self):
        return self.__repr__()


my_queue = Queue()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)
print(my_queue.dequeue().get_data())
print(my_queue.size())

