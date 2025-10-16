# Example 1: Using `is`
print("\n====+==== Using `is` ====+====")
Num1 = [1, 2, 3]
Num2 = Num1
Num3 = [1, 2, 3]

print(f"{Num1} is {Num2} → {Num1 is Num2}")   # True, same object
print(f"{Num1} is {Num3} → {Num1 is Num3}")   # False, different object
print(f"{Num1} == {Num3} → {Num1 == Num3}")   # True, values are equal

# Example 2: Using `is not`
print("\n====+==== Using `is not` ====+====")
a = 10
b = 20

print(f"{a} is not {b} → {a is not b}")    # True
print(f"{a} is not 10 → {a is not 10}")  # False, small integers cached

# Example 3: Checking for None
print("\n====+==== Checking for None ====+====")
Num1 = None
print(f"{Num1} is None → {Num1 is None}")      # True
