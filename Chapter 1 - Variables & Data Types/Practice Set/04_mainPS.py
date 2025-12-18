num1 = float(input("Enter the Num1:= "))
num2 = float(input("Enter the Num2:= "))
print("====*====*====*====\n")

if num1 == num2:
    print(f"{num1} == {num2}:= Both are Equal")
elif num1 > num2:
    print(f"{num1} > {num2}:= {num1} is Greater than {num2}")
else:
    print(f"{num1} < {num2} := {num2} is Greater than {num1}")