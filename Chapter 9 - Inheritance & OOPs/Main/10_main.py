# -----------------------------------------------------
#     🔥 ALL-TIME BEST PYTHON MULTI-UTILITY PROGRAM 🔥
# -----------------------------------------------------

import os

# Colors for Premium UI
class Color:
    HEADER = "\033[95m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    CYAN = "\033[96m"
    BOLD = "\033[1m"
    END = "\033[0m"


# Calculator Class
class Calculator:
    def __init__(self, a, b=None):
        self.a = a
        self.b = b

    def add(self): return self.a + self.b
    def sub(self): return self.a - self.b
    def mul(self): return self.a * self.b
    def div(self): return "❌ Cannot divide by zero!" if self.b == 0 else self.a / self.b
    def mod(self): return "❌ Cannot modulo by zero!" if self.b == 0 else self.a % self.b
    def exp(self): return self.a ** self.b


# Extra Functions
def factorial(n):
    if n < 0:
        return "❌ Factorial not defined for negative numbers!"
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

def print_table(n):
    lines = []
    for i in range(1, 11):
        lines.append(f"{n} x {i} = {n*i}")
    return "\n".join(lines)

def is_prime(n):
    if n <= 1:
        return "❌ Not Prime"
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return "❌ Not Prime"
    return "✔ Prime Number"

def even_odd(n):
    return "✔ Even" if n % 2 == 0 else "✔ Odd"

def clear():
    os.system("cls" if os.name == "nt" else "clear")


# Menu
def menu():
    print(Color.CYAN + Color.BOLD + "\n========== MASTER MENU ==========" + Color.END)
    print(Color.GREEN + " 1. Calculator")
    print(" 2. Print Table")
    print(" 3. Factorial")
    print(" 4. Prime Check")
    print(" 5. Even/Odd Check")
    print(" 6. Square & Cube")
    print(" 0. Exit" + Color.END)
    print(Color.CYAN + "===================================" + Color.END)


# Main Loop
while True:
    try:
        clear()
        print(Color.HEADER + Color.BOLD + "\n🔥 ALL-TIME BEST PYTHON TOOLBOX 🔥" + Color.END)

        menu()
        choice = input(Color.YELLOW + "\nEnter your choice: " + Color.END).strip()

        print(Color.CYAN + "\n----------- RESULT -----------" + Color.END)

        # --------------------------------#
        # 1. Calculator
        # --------------------------------#
        if choice == "1":
            a = float(input("Enter Number 1: "))
            b = float(input("Enter Number 2: "))
            calc = Calculator(a, b)

            print("\nAvailable Operations:")
            print("+  -  *  /  %  ^  all")

            op = input("Choose operation: ").strip().lower()

            if op == "+":
                print(f"{a} + {b} = {calc.add()}")
            elif op == "-":
                print(f"{a} - {b} = {calc.sub()}")
            elif op == "*":
                print(f"{a} * {b} = {calc.mul()}")
            elif op == "/":
                print(f"{a} / {b} = {calc.div()}")
            elif op == "%":
                print(f"{a} % {b} = {calc.mod()}")
            elif op == "^":
                print(f"{a} ^ {b} = {calc.exp()}")
            elif op == "all":
                print(f"Addition:       {calc.add()}")
                print(f"Subtraction:    {calc.sub()}")
                print(f"Multiplication: {calc.mul()}")
                print(f"Division:       {calc.div()}")
                print(f"Modulo:         {calc.mod()}")
                print(f"Exponent:       {calc.exp()}")
            else:
                print(Color.RED + "❌ Invalid Operation!" + Color.END)

        # --------------------------------#
        # 2. Print Table
        # --------------------------------#
        elif choice == "2":
            n = int(input("Enter number: "))
            print("\n" + print_table(n))

        # --------------------------------#
        # 3. Factorial
        # --------------------------------#
        elif choice == "3":
            n = int(input("Enter number: "))
            print(f"Factorial of {n} = {factorial(n)}")

        # --------------------------------#
        # 4. Prime Check
        # --------------------------------#
        elif choice == "4":
            n = int(input("Enter number: "))
            print(is_prime(n))

        # --------------------------------#
        # 5. Even/Odd Check
        # --------------------------------#
        elif choice == "5":
            n = int(input("Enter number: "))
            print(even_odd(n))

        # --------------------------------#
        # 6. Square & Cube
        # --------------------------------#
        elif choice == "6":
            n = float(input("Enter number: "))
            print(f"Square of {n} = {n*n}")
            print(f"Cube of {n}   = {n*n*n}")

        # --------------------------------#
        # Exit
        # --------------------------------#
        elif choice == "0":
            print(Color.RED + "\n👋 Thank you for using the Master Program!" + Color.END)
            break

        else:
            print(Color.RED + "❌ Invalid Choice!" + Color.END)

        print(Color.CYAN + "-------------------------------\n" + Color.END)
        input(Color.YELLOW + "Press ENTER to continue..." + Color.END)

    except ValueError:
        print(Color.RED + "\n❌ Error: Enter valid numbers only!" + Color.END)
        input(Color.YELLOW + "Press ENTER to retry..." + Color.END)
