with open("Chapter 7 - File I or O/Practice Set/numbers.txt", "r") as f:
    data = f.read()

# Use split() to separate numbers by comma
parts = data.split(",")

even_count = 0
odd_count = 0

for p in parts:
    num = int(p)        # convert to integer
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"Count of Even numbers:= {even_count}")
print(f"Count of Odd numbers:= {odd_count}")