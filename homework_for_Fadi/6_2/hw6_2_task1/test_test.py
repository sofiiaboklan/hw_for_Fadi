"""
Task 1: Imports practice
Make a directory with 2 modules; make a function in one of them; then import this function in the other module
and use that in your script of choice.
"""

print("\nTASK ONE\n")

from test_function import make_words_bigger

test_word = input("Put in one word and we will make it uppercase for you: ")
make_words_bigger(f"{test_word}")