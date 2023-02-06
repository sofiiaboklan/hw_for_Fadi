with open('user_info.txt') as file_object:
    username = file_object.read()
print("Hello again, " + username + "!")
