# Function to calculate factorial of a number recursively
def calculate_factorial(number):
    if number == 0 or number == 1:
        return 1
    return number * calculate_factorial(number - 1)

# Asking user for a number
num = int(input("Enter a number to calculate its factorial: "))

# Displaying the result
print(f"The factorial of {num}: {calculate_factorial(num)}")
