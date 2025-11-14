# Define the name string
name = "Aman Patidar"

# Full Name index Start to End
print(f"Full Name: {name[:]}")
print("====+"*3 + "===="*1)

# Slice from index 2 to 8 (includes 2, excludes 8)
print(f"Slice [2:8]: {name[2:8]}")
print("====+"*3 + "===="*1)

# Slice from the beginning to index 8 (includes 0, excludes 8)
print(f"Slice [:8]: {name[:8]}")
print("====+"*3 + "===="*1)

# Slice from index 2 to the end of the string
print(f"Slice [2:]: {name[2:]}")
print("====+"*3 + "===="*1)

# Slice the string with a step of 2, getting every second character
print(f"Slice [::2]: {name[::2]}")
print("====+"*3 + "===="*1)

# Slice the string in reverse order with a step of -2, getting every second character backwards
print(f"Slice [::-2]: {name[::-2]}")
print("====+"*3 + "===="*1)

# Reverse the entire string and get every third character from it
print(f"Reversed & Slice [::-2]: {name[::-2]}")  
print("====+"*3 + "===="*1)

# Slice from index 2 to 10 with a step of 2, getting every third character between index 2 and 9
print(f"Slice [2:10:2]: {name[::1]}")
print("====+"*3 + "===="*1)

# Slice from index 1 to 6 and reverse it (so, we reverse only a part of the string)
print(f"Slice [1:6][::-1]: {name[::-1]}")
print("====+"*3 + "===="*1)

# Slice the first word, 'Aman Patidar', and transform it to uppercase
print(f"word to uppercase: {name.upper()}")
print("====+"*3 + "===="*1)

# Slice the second word, 'Aman Patidar', and make it lowercase
print(f"word to lowercase: {name.lower()}")
print("====+"*3 + "===="*1)

# Combining slices: Get the first part, skip the space, then get the second part
print(f"Combined slices (first & second words without space): {name[:4] + name[5:]}")
print("====+"*3 + "===="*1)