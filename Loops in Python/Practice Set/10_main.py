# Program to print a diamond pattern

# Asking user for the number of rows in the top half of the diamond
rows = int(input("Enter the number of rows for the diamond: "))

# Top half of the diamond
for i in range(1, rows + 1):
    print("  " * (rows - i) + "* " * (2 * i - 1))

# Bottom half of the diamond
for i in range(rows - 1, 0, -1):
    print("  " * (rows - i) + "* " * (2 * i - 1))