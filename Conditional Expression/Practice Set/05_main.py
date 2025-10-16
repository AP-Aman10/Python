# List of names
name_list = ["Aman Patidar", "Prince Patidar", "Shubham Patidar", "Preet Patidar"]

# Asking user for their name
user_name = input("Enter your name: ")

# Checking if the name is in the list
if user_name in name_list:
    print(f"{user_name}, your name is in the list.")
else:
    print(f"{user_name}, your name is not in the list.")
