def calculate_average():
    while True:
        try:
            num = int(input("Please enter how many numeric values you want to average:= "))
            if num <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter an integer.")
    
    total = 0.0
    
    for i in range(1, num + 1):
        while True:
            try:
                value = float(input(f"Enter number {i}: "))
                total += value
                break
            except ValueError:
                print("Invalid input! Please enter a numeric value.")
    
    average = total / num
    
    print("====*====*====*====")
    print(f"Total of values: {total}")
    print(f"Average of values: {average:.2f}")
    print("====*====*====*====*====*====*====*====")


# Ask user how many times to run the calculation
while True:
    try:
        userinput = int(input("How many times do you want to run the calculation:= "))
        if userinput <= 0:
            print("Please enter a positive integer.")
            continue
        break
    except ValueError:
        print("Invalid input! Please enter an integer.")

for _ in range(userinput):
    calculate_average()
    print("Thank you — I really appreciate your help!\n")
