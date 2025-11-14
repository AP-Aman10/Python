# Asking user for a number
number = int(input("Enter a number to print its multiplication table: "))

# Initialize multiplier
multiplier = 1

# Print multiplication table from 1 to 10
while multiplier <= 10:
    print(f"{number} x {multiplier} = {number * multiplier}")
    multiplier += 1
    
print(f"Multiplier table using While Loop")