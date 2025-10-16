# Program to print a pyramid pattern of stars

# Asking user for the number of rows
rows = int(input("Enter the number of rows for the pyramid: "))

# Loop to print each row
for i in range(1, rows + 1):
    # Print spaces
    print("  " * (rows - i), end="")
    # Print stars
    print("* " * (2 * i - 1), end="")
    # Move to the next line
    print("")
