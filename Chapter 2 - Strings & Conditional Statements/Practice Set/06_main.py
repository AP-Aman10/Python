# Asking user for a username
user_name = input("Enter your username: ")

# Checking the length of the username
if len(user_name) < 10:
    print("Your username has less than 10 characters.")
else:
    print("Your username has 10 or more characters.")