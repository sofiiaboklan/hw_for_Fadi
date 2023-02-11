"""
Task 1: Files
Write a script that creates a new output file called myfile.txt and writes the string "Hello file world!" in it.
Then write another script that opens myfile.txt, and reads and prints its contents.
Run your two scripts from the system command line.

1) Does the new file show up in the directory where you ran your scripts?
2) What if you add a different directory path to the filename passed to open?
"""

print("\nTASK ONE\n")

with open('myfile.txt', 'w') as file_object:
    file_object.write("Hello file world!")

with open('myfile.txt', 'r') as file_object:
    print(file_object.read())  # I did this in another script, and it worked the same as it did here.

# 1) Yes, the new file showed up in the directory where I ran my scripts
# 2) I can do it by writing out the whole path like this:

# path = '/Users/macbookair/PycharmProjects/pythonProject1/homework for Fadi/random_dir/myfile.txt'
# with open(path, 'w') as file_object:
#    file_object.write("Hello file world!")

# However, if I write the path incorrectly, it won't create a file (or a new directory to store that file in).