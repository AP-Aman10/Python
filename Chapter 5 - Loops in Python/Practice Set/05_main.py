# Asking user for a number
number = int(input("Enter a number to calculate the sum from 1 to n: "))

# Initialize variables
counter = 1
total_sum = 0

# Using while loop to calculate sum
while counter <= number:
    total_sum += counter
    counter += 1

print(f"The sum of numbers from 1 to {number}:= {total_sum}")
