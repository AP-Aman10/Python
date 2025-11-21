# Program to calculate factorial of a number

# Asking user for a number
number = int(input("Enter a number to calculate its factorial: "))

# Initialize factorial
factorial = 1

# Calculate factorial using a for loop
for i in range(1, number + 1):
    factorial *= i  # same as factorial = factorial * i

print(f"The factorial of {number}:= {factorial}")
