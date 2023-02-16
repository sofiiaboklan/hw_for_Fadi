"""
Task 3: Basics, import, work with os module

Write a program that counts lines and characters in a file
Create a Python module called `mymod.py`, which has three functions:

1) count_lines(name) function that reads an input file and counts the number of lines in it (hint: file.readlines()
does most of the work for you, and `len` does the rest)
2) count_chars(name) function that reads an input file and counts the number of characters in it (hint: file.read()
returns a single string)
3) test(name) function that calls both counting functions with a given input filename.
Such a filename generally might be passed-in, hard-coded, input with raw_input, or pulled from a command-line
via the sys.argv list; for now, assume it’s a passed-in function argument.

All three `mymod.py` functions should expect a filename string to be passed in.
Test your module interactively, using import and name qualification to fetch your exports.
Does your PYTHONPATH need to include the directory where you created mymod.py?

Try running your module on itself: e.g., test("mymod.py").
Note that the test opens the file twice; if you’re feeling ambitious, you may be able to improve this
by passing an open file object into the two count functions (hint: file.seek(0) is a file rewind).
"""

print("\nTASK THREE\n")

from mymod import count_lines, count_chars, test

# If the module is in the same directory - then no, I don't have to include the directory.
# However, if it is in some other one, I would have to do the following code:

# import sys
# sys.path.append('/Users/macbookair/PycharmProjects/pythonProject1/homework_for_Fadi/random_dir_with_mymod')
# from mymod import count_lines, count_chars, test

print("Testing the functions 1 and 2:\n")

count_lines('o_captain.txt')

count_chars('o_captain.txt')

print("\nTesting the third function that combines the first two:\n")

test('o_captain.txt')