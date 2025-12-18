def factorial(x):
    """Return the factorial of n using recursion."""
    if x == 0 or x == 1:
        return 1
    return x * factorial(x - 1)


# --- Main Program ---
print("📌 Factorial Calculator")

while True:
    try:
        user_input = int(input("Enter a non-negative integer:= "))

        if user_input < 0:
            print("❌ Factorial does not exist for negative numbers. Try again.\n")
            continue

        print(f"✔ The factorial of {user_input}:= {factorial(user_input)}")
        break

    except ValueError:
        print("❌ Invalid input! Please enter a valid integer.\n")
