# Function to convert inches to centimeters
def convert_inches_to_centimeters(inches):
    return inches * 2.54

# Function to convert centimeters to inches
def convert_centimeters_to_inches(centimeters):
    return centimeters / 2.54

# Asking user for the conversion type
print("Choose conversion type:")
print("1. Inches ➜ Centimeters")
print("2. Centimeters ➜ Inches")

choice = input("Enter 1 or 2: ")

# Performing the conversion based on user choice
if choice == "1":
    inches_value = float(input("Enter value in inches: "))
    result = convert_inches_to_centimeters(inches_value)
    print(f"{inches_value} inches = {round(result, 2)} cm")

elif choice == "2":
    cm_value = float(input("Enter value in centimeters: "))
    result = convert_centimeters_to_inches(cm_value)
    print(f"{cm_value} cm = {round(result, 2)} inches")

else:
    print("Invalid choice. Please enter 1 or 2.")