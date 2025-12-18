lst = list(map(int, input("Enter list elements separated by space: ").split()))

if lst == lst[::-1]:
    print("The list is a palindrome")
else:
    print("The list is not a palindrome")
