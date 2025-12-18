# Asking user for their age
user_age = int(input("Enter your age: "))
print()

# If-elif-else ladder to check age
if user_age >= 18:
    print("You are an adult.")
    print("You are eligible for certain privileges.")
elif user_age < 0:
    print("Invalid input! Age cannot be negative.")
elif user_age == 0:
    print("Age cannot be 0. Please enter a valid age.")
else:
    print("You are a minor.")
    print("Some activities are restricted for you.")
print()

print("Program ended.")