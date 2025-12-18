# Program to print a hollow square pattern of stars

# Asking user for the size of the square
size = int(input("Enter the size of the square: "))

# Loop to print each row
for row in range(1, size + 1):
    if row == 1 or row == size:
        # Print the first and last row completely filled
        print("* " * size)
    else:
        # Print the hollow rows
        print("* " + "  " * (size - 2) + "*")
