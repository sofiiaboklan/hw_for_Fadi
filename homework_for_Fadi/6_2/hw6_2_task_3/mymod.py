def count_lines(file):
    num_lines = 0
    with open(file, 'r') as f:
        for line in f:
            num_lines += 1
    print("Number of lines in text file: ", num_lines)


# count_lines('o_captain.txt')


def count_chars(file):
    with open(file, 'r') as f:
        data = f.read()
        number_of_characters = len(data)
        print('Number of characters in text file :', number_of_characters)


# count_chars('o_captain.txt')


def test(file):
    count_lines(file)
    count_chars(file)


# test('o_captain.txt')

# test('mymod.py')  # I'm sorry, I didn't feel ambitious enough to make it only run once...
