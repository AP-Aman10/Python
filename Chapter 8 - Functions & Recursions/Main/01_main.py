# Function to calculate the average of four numbers
def calculate_average():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))
    num4 = int(input("Enter the fourth number: "))
    
    average = (num1 + num2 + num3 + num4) / 4
    print(f"The average of the four numbers: {average:.2f}")

# Calling the function multiple times
calculate_average()
print("Thank you!\n")

calculate_average()
print("Thank you!\n")

calculate_average()
print("Thank you!\n")
