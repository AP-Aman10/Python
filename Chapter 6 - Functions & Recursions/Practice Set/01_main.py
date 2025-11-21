# Function to find the largest of four numbers
def get_largest_number(X_1, X_2, X_3, X_4):
    if X_1 >= X_2 and X_1 >= X_3 and X_1 >= X_4:
        return X_1
    elif X_2 >= X_1 and X_2 >= X_3 and X_2 >= X_4:
        return X_2
    elif X_3 >= X_1 and X_3 >= X_2 and X_3 >= X_4:
        return X_3
    else:
        return X_4

# Asking user for input
first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))
third_num = int(input("Enter the third number: "))
fourth_num = int(input("Enter the fourth number: "))

# Displaying the result
print(f"The largest number := {get_largest_number(first_num, second_num, third_num, fourth_num)}")