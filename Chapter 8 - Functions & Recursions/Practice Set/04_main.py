# Function to print a descending star pattern using recursion
def print_descending_pattern(rows):
    if rows == 0:
        return
    print("* " * rows)
    print_descending_pattern(rows - 1)

# Asking user for input
num_rows = int(input("Enter the number of rows: "))

# Displaying the pattern
print_descending_pattern(num_rows)