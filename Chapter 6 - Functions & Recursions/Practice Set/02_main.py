# Function to convert Fahrenheit to Celsius
def convert_fahrenheit_to_celsius(fahrenheit_temperature):
    return (fahrenheit_temperature - 32) * 5 / 9

# Function to convert Celsius to Fahrenheit
def convert_celsius_to_fahrenheit(celsius_temperature):
    return (celsius_temperature * 9 / 5) + 32

# Asking user which conversion they want
print("Temperature Converter")
print("1. Fahrenheit to Celsius")
print("2. Celsius to Fahrenheit")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))
    celsius_result = convert_fahrenheit_to_celsius(fahrenheit_input)
    print(f"The temperature in Celsius is: {round(celsius_result, 2)}°C")

elif choice == "2":
    celsius_input = float(input("Enter temperature in Celsius: "))
    fahrenheit_result = convert_celsius_to_fahrenheit(celsius_input)
    print(f"The temperature in Fahrenheit is: {round(fahrenheit_result, 2)}°F")

else:
    print("Invalid choice! Please enter 1 or 2.")
