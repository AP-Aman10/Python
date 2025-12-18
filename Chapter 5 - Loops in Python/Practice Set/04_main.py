# Asking user for a number
number = int(input("Enter a number to check if it is prime: "))

# Prime check
if number < 2:
    print(f"{number} is not a prime number.")
else:
    for divisor in range(2, number):
        if number % divisor == 0:
            print(f"{number} is not a prime number.")
            break
    else:
        print(f"{number} is a prime number.")
