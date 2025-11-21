# Asking user for their age
user_age = int(input("Enter your age: "))

# Check if the age is even
if user_age % 2 == 0:
    print(f"{user_age} is an even number.")
print()

# Check age categories
if user_age >= 18:
    print("You are an adult.")
    print("You are eligible for certain privileges.")
elif user_age < 0:
    print("Invalid input! Age cannot be negative.")
else:
    print("You are a minor.")
    print("Some activities are restricted for you.")
print()

print("Program ended.")