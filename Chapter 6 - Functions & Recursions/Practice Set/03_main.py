def calculate_sum_upto(x):
    return x * (x + 1) // 2

def main():
    print("📌 Sum of First N Natural Numbers")

    while True:
        user_input = input("Enter a positive integer (or 'q' to quit):= ")

        if user_input.lower() == 'q':
            print("Goodbye!")
            break

        try:
            user_input = int(user_input)

            if user_input < 0:
                print("❌ Please enter a positive integer.\n")
                continue

            total = calculate_sum_upto(user_input)
            print(f"✅ The sum of numbers from 1 to {user_input}:= {total}\n")

        except ValueError:
            print("❌ Invalid input! Please enter a valid integer.\n")

# Run the program
main()
