# Recursive function to calculate the sum of first n natural numbers
def calculate_sum_upto(number):
    if number == 1:
        return 1
    return calculate_sum_upto(number - 1) + number

# Asking user for input
num = int(input("Enter a number to find the sum up to: "))

# Calculating and displaying result
print(f"The sum of numbers from 1 to {num} is: {calculate_sum_upto(num)}")
