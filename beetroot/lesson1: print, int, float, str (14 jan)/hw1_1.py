# Task 2

# Exp output: Hello Fadi
print("Hello Fadi")

# End and Sep are optional parameters of Python.
# The end parameter basically prints after all the output objects present in one output statement have been returned.
# The sep parameter differentiates between the objects.

# Exp output: '1, 2, 3' '1 2 3,'
a = 1
b = 2
c = a + b
print(a, b, c, sep = ",")

print(a, b, c, end = ",")

# Task 3

# the backslash "\" is a special character, also called the "escape" character.
# It is used in representing certain whitespace characters:
# "\t" is a tab, "\n" is a newline, and "\r" is a carriage return.

print("\n\n#########")
print("#\t\t#")
print("#\t\t#")
print("#\t\t#")
print("#########")

print("\n#\t\t#")
print("#\t\t#")
print("#########")
print("#\t\t#")
print("#\t\t#")

# Another (easier) version - for me

a = """
#########
#       #
#       #
#       #
#########
"""
print(a)

a = """
#       #
#       #
#########
#       #
#       #
"""
print(a)
