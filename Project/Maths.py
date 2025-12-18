# --------------------------------------------------------
#        🔥 ULTIMATE PRO MAX PYTHON TOOLBOX (COLORED) 🔥
# --------------------------------------------------------

import os

# ========== Colors ==========
class Color:
    BOLD = "\033[1m"
    HEADER = "\033[95m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    END = "\033[0m"


# ========== Utility: Clear Screen ==========
def clear():
    os.system("cls" if os.name == "nt" else "clear")


# ========== Calculator Class ==========
class Calculator:
    def __init__(self, Value1, Value2=None):
        self.Value1 = Value1
        self.Value2 = Value2

    def add(self): return self.Value1 + self.Value2
    def sub(self): return self.Value1 - self.Value2
    def mul(self): return self.Value1 * self.Value2

    def div(self):
        if self.Value2 == 0:
            return Color.RED + "Error: Division by zero!" + Color.END
        return self.Value1 / self.Value2

    def mod(self):
        if self.Value2 == 0:
            return Color.RED + "Error: Modulo by zero!" + Color.END
        return self.Value1 % self.Value2

    def exp(self): return self.Value1 ** self.Value2


# ========== Math Utilities ==========
def factorial(num):
    if num < 0:
        return Color.RED + "Error: Factorial of negative number not allowed!" + Color.END
    f = 1
    for i in range(1, num + 1): f *= i
    return f

def multiplication_table(num, upto=10):
    return "\n".join([f"{num} x {i} = {num * i}" for i in range(1, upto + 1)])

def is_prime(num):
    if num <= 1: return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0: return False
    return True

def is_even(num): return num % 2 == 0
def square(num): return num * num
def cube(num): return num * num * num

def reverse_number(num):
    return int(str(abs(num))[::-1]) * (1 if num >= 0 else -1)

def sum_of_digits(num):
    return sum(int(d) for d in str(abs(num)))

def is_armstrong(num):
    digits = str(num)
    power = len(digits)
    return num == sum(int(d) ** power for d in digits)

def fibonacci(num):
    if num <= 0:
        return Color.RED + "Enter Value1 positive number!" + Color.END
    seq = [0, 1]
    for _ in range(2, num): seq.append(seq[-1] + seq[-2])
    return seq[:num]

def is_perfect(num):
    if num <= 0: return False
    return num == sum(i for i in range(1, num) if num % i == 0)


# ========== Menu ==========
def show_menu():
    print(Color.CYAN + Color.BOLD + "\n=========== ULTIMATE TOOLBOX ===========" + Color.END)
    print(Color.RED + Color.BOLD + " 1. Calculator")
    print(" 2. Print Table")
    print(" 3. Factorial")
    print(" 4. Prime Check")
    print(" 5. Even/Odd Check")
    print(" 6. Square & Cube")
    print(" 7. Armstrong Number Check")
    print(" 8. Reverse Number")
    print(" 9. Sum of Digits")
    print("10. Fibonacci Series")
    print("11. Perfect Number Check")
    print(" 0. Exit" + Color.END)
    print(Color.CYAN + Color.BOLD +"========================================" + Color.END)


# ========== Main Program ==========
while True:
    try:
        clear()
        print(Color.HEADER + Color.BOLD + "🔥 WELCOME TO COLORED ULTIMATE TOOLBOX 🔥" + Color.END)

        show_menu()
        choice = input(Color.YELLOW + "\nEnter your choice: " + Color.END).strip()

        print(Color.BLUE + Color.BOLD + "\n------------- RESULT -------------" + Color.END)

        # ---------------------------------- Calculator
        if choice == "1":
            Value1 = float(input("Enter number 1: "))
            Value2 = float(input("Enter number 2: "))
            calc = Calculator(Value1, Value2)

            print("\nOperations: +  -  *  /  %  ^  all")
            op = input("Choose operation: ").strip()

            if op == "+": print(Color.GREEN + f"Result = {calc.add()}" + Color.END)
            elif op == "-": print(Color.GREEN + f"Result = {calc.sub()}" + Color.END)
            elif op == "*": print(Color.GREEN + f"Result = {calc.mul()}" + Color.END)
            elif op == "/": print(Color.GREEN + f"Result = {calc.div()}" + Color.END)
            elif op == "%": print(Color.GREEN + f"Result = {calc.mod()}" + Color.END)
            elif op == "^": print(Color.GREEN + f"Result = {calc.exp()}" + Color.END)
            elif op.lower() == "all":
                print(Color.GREEN + f"Add:        {calc.add()}")
                print(f"Subtract:   {calc.sub()}")
                print(f"Multiply:   {calc.mul()}")
                print(f"Divide:     {calc.div()}")
                print(f"Modulo:     {calc.mod()}")
                print(f"Exponent:   {calc.exp()}" + Color.END)
            else:
                print(Color.RED + "Invalid operation!" + Color.END)

        # ---------------------------------- Table
        elif choice == "2":
            num = int(input("Enter number: "))
            print(Color.CYAN + Color.BOLD + "\n" + multiplication_table(num) + Color.END)

        # ---------------------------------- Factorial
        elif choice == "3":
            num = int(input("Enter number: "))
            print(Color.GREEN + Color.BOLD + f"Factorial = {factorial(num)}" + Color.END)

        # ---------------------------------- Prime Check
        elif choice == "4":
            num = int(input("Enter number: "))
            print(Color.GREEN + Color.BOLD + ("Prime" if is_prime(num) else "Not Prime") + Color.END)

        # ---------------------------------- Even/Odd
        elif choice == "5":
            num = int(input("Enter number: "))
            print(Color.GREEN + Color.BOLD + ("Even" if is_even(num) else "Odd") + Color.END)

        # ---------------------------------- Square & Cube
        elif choice == "6":
            num = float(input("Enter number: "))
            print(Color.GREEN + Color.BOLD + f"Square = {square(num)}")
            print(f"Cube   = {cube(num)}" + Color.END)

        # ---------------------------------- Armstrong
        elif choice == "7":
            num = int(input("Enter number: "))
            print(Color.GREEN + Color.BOLD + ("Armstrong" if is_armstrong(num) else "Not Armstrong") + Color.END)

        # ---------------------------------- Reverse Number
        elif choice == "8":
            num = int(input("Enter number: "))
            print(Color.GREEN + Color.BOLD + f"Reversed = {reverse_number(num)}" + Color.END)

        # ---------------------------------- Sum of Digits
        elif choice == "9":
            num = int(input("Enter number: "))
            print(Color.GREEN + Color.BOLD + f"Sum = {sum_of_digits(num)}" + Color.END)

        # ---------------------------------- Fibonacci
        elif choice == "10":
            num = int(input("Enter limit: "))
            print(Color.GREEN + Color.BOLD + f"Fibonacci: {fibonacci(num)}" + Color.END)

        # ---------------------------------- Perfect Number
        elif choice == "11":
            num = int(input("Enter number: "))
            print(Color.GREEN + Color.BOLD + ("Perfect Number" if is_perfect(num) else "Not Perfect") + Color.END)

        # ---------------------------------- Exit
        elif choice == "0":
            print(Color.RED + Color.BOLD + "\nThank you for using the Toolbox! 👋" + Color.END)
            break

        else:
            print(Color.RED + Color.BOLD + "Invalid choice!" + Color.END)

        print(Color.BLUE + Color.BOLD + "----------------------------------\n" + Color.END)
        input(Color.YELLOW + Color.BOLD + "Press ENTER to continue..." + Color.END)

    except ValueError:
        print(Color.RED + Color.BOLD + "\nError: Enter valid numbers only!" + Color.END)
        input(Color.YELLOW + Color.BOLD + "Press ENTER to retry..." + Color.END)
