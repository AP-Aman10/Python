# Bitwise Operators
print("====*==== Bitwise Operators ====+====")
num1 = int(input("Enter the num1: "))
num2 = int(input("Enter the num2: "))
print(f"{num1} & {num2} (AND)    : {num1 & num2}")  # 0001 = 1
print(f"{num1} | {num2} (OR)     : {num1 | num2}")  # 0111 = 7
print(f"{num1} ^ {num2} (XOR)    : {num1 ^ num2}")  # 0110 = 6
print(f"~{num1} (NOT)       : {~num1}")     # Inverts bits
print(f"{num1} << 1 (Left shift)  : {num1 << 1}")
print(f"{num1} >> 1 (Right shift) : {num1 >> 1}")