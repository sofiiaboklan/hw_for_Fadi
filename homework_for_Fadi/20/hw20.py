"""
Task 1: File Context Manager class
Create your own class, which can behave like a built-in function `open`.
Also, you need to extend its functionality with counter and logging.

Pay special attention to the implementation of `__exit__` method, which has to cover all the requirements to
context managers mentioned here:

Context Manager Types
The with statement
"""

print("\nTASK ONE\n")


class MyCounter(object):
    counter = 0

    def __init__(self, file_name, method):
        try:
            self.file_obj = open(file_name, method)
            print("Initialisation")
        except FileNotFoundError:
            self.file_obj = None

    @classmethod
    def get_num_of_usage(cls):
        return cls.counter

    def __enter__(self):
        if self.file_obj is None:
            raise FileNotFoundError("File not found :(")
        MyCounter.counter += 1
        print("Entering MyCounter")
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print("Some exception was thrown")
        print(f'Closing context, number of contexts is {self.counter}')
        if self.file_obj is not None:
            self.file_obj.close()
        return None


with MyCounter('temp.txt', 'r') as opened_file:
    data = opened_file.read()
    print("\n" + data)

with MyCounter('temp.txt', 'r') as opened_file:
    data = opened_file.read()
    print("\n" + data)

"""
Task 2: Writing tests for context manager
Take your implementation of the context manager class from Task 1 and write tests for it. 
Try to cover as many use cases as you can, positive ones when a file exists and everything works as designed. 
And also, write tests when your class raises errors or you have errors in the runtime context suite.
"""

print("\nTASK TWO\n")

import unittest


class TestFile(unittest.TestCase):
    def test_open_file(self):
        with MyCounter('temp.txt', 'r') as opened_file:
            self.assertNotEqual(opened_file, None)

    def test_open_unextisting_file(self):
        try:
            with MyCounter('temp1.txt', 'r') as opened_file:
                self.assertEqual(opened_file, None)
        except:
            self.assertRaises(FileNotFoundError)
