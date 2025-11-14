# Function to find the largest of four numbers
def get_largest_number(first_num, second_num, third_num, fourth_num):
    if first_num >= second_num and first_num >= third_num and first_num >= fourth_num:
        return first_num
    elif second_num >= first_num and second_num >= third_num and second_num >= fourth_num:
        return second_num
    elif third_num >= first_num and third_num >= second_num and third_num >= fourth_num:
        return third_num
    else:
        return fourth_num

# Asking user for input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
num4 = int(input("Enter the fourth number: "))

# Displaying the result
print(f"The largest number is: {get_largest_number(num1, num2, num3, num4)}")