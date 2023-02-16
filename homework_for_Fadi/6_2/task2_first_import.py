"""
Task 2: The sys module.

The “sys.path” list is initialized from the PYTHONPATH environment variable.
Is it possible to change it from within Python? If so, does it affect where Python looks for module files?
Run some interactive tests to find it out.
"""

print("\nTASK TWO\n")

# Yes, you can change the PYTHONPATH since it ends up in a sys.path, which is a list of directories that should be
# searched for Python packages, so you can just append your directories to that list
# like: "sys.path.append('/path/to/something')".

# Yes, it affects where Python looks for module files, since you set the path to them.
# When a module is imported within a Python file, the interpreter first searches for the specified module among
# its built-in modules. If not found it looks through the list of directories defined by sys.path,
# which is why we append it with the needed directories.

import sys

sys.path.append('/Users/macbookair/PycharmProjects/pythonProject1/homework_for_Fadi/6_2/hw6_2_task2')

import test_sys_path

print(test_sys_path.surprise_print)

# It worked!
