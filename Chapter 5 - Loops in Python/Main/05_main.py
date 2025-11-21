Value = [2, 4, 10, 20, 45, 47, 64, 81, 96, 100]

for number in Value:
    if number == 45:
        break
    print(f"Number:= {number}")
print(f"====*==== Brack End ====*====\n")

Value = [2, 4, 10, 20, 45, 47, 64, 81, 96, 100]

for number in Value:
    if number == 45:
        continue
    print(f"Number:= {number}")
print(f"====*==== Continue End ====*====\n")