# Asking user for four numbers
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))

# Finding the greatest number
if num1 == num2 == num3 == num4:
    print(f"All numbers are equal: {num1}")
elif num1 > num2 and num1 > num3 and num1 > num4:
    print(f"The greatest number: {num1}")
elif num2 > num1 and num2 > num3 and num2 > num4:
    print(f"The greatest number: {num2}")
elif num3 > num1 and num3 > num2 and num3 > num4:
    print(f"The greatest number: {num3}")
elif num4 > num1 and num4 > num2 and num4 > num3:
    print(f"The greatest number: {num4}")
else:
    print(f"There is a tie among the greatest numbers.")
