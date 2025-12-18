# Program to print a right-angled triangle of stars

# Asking user for the number of rows
rows = int(input("Enter the number of rows for the triangle: "))

# Loop to print each row
for i in range(1, rows + 1):
    print("* " * i)  # print i stars for the i-th row