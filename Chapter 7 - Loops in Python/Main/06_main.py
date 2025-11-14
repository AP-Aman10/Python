# Example using break: stops the loop when number reaches 34
for number in range(100):
    if number == 10+1:
        break  # exit the loop immediately
    print(number)

print("\n")  # Just to separate outputs

# Example using continue: skips the number 34 but continues the loop
for number in range(100):
    if number == 2 or number == 4 or number == 10 or number == 20 or number == 45 or number == 47 or number == 64 or number == 81 or number == 96 or number == 100:
        continue  # skip this iteration
    print(number)
