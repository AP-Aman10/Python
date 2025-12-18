def fibonacci(X):
    if X <= 1:
        return X
    return fibonacci(X - 1) + fibonacci(X - 2)

user_input = int(input("Enter how many Fibonacci numbers you want:= "))

fib_list = []

for i in range(user_input):
    fib_list.append(fibonacci(i))

print(" → ".join(map(str, fib_list)))
