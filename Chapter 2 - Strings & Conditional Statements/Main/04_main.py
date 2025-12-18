# Asking user for their age
user_age = int(input("Enter your age: "))
print()

# Checking if the user is an adult
if user_age >= 18:
    print("You are an adult.")
    print("You are eligible for certain privileges.")
else:
    print("You are a minor.")
    print("Some activities are restricted for you.")
print()

print("Program ended.")