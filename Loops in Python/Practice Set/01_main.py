# Asking user for a number
number = int(input("Enter a number to print its multiplication table: "))

# Printing multiplication table from 1 to 10
for multiplier in range(1, 10+1):
    print(f"{number} x {multiplier} = {number * multiplier}")