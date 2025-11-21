# OOP = Object Oriented Programming
class Calculator:
    def add(self, X, Y):
        return X + Y

    def subtract(self, X, Y):
        return X - Y

    def multiply(self, X, Y):
        return X * Y

    def divide(self, X, Y):
        if Y == 0:
            return "Error: Division by zero!"
        return X / Y

    def modulus(self, X, Y):
        if Y == 0:
            return "Error: Modulus by zero!"
        return X % Y

    def power(self, X, Y):
        return X ** Y


# --- Main Program ---
if __name__ == "__main__":
    calc = Calculator()

    while True:
        op = input("Enter operation (+, -, *, /, %, ^) or 'exit' to quit: ")

        if op.lower() == "exit":
            print("Exiting Calculator. Goodbye!")
            break

        try:
            Value1 = float(input("Enter Value1 number: "))
            Value2 = float(input("Enter Value2 number: "))

            if op == '+':
                result = calc.add(Value1, Value2)
            elif op == '-':
                result = calc.subtract(Value1, Value2)
            elif op == '*':
                result = calc.multiply(Value1, Value2)
            elif op == '/':
                result = calc.divide(Value1, Value2)
            elif op == '%':
                result = calc.modulus(Value1, Value2)
            elif op == '^':
                result = calc.power(Value1, Value2)
            else:
                result = "Invalid operation!"

            if isinstance(result, (int, float)):
                print(f"Result: {result:.2f}")
            else:
                print(result)

        except ValueError:
            print("Error: Please enter valid numbers!")