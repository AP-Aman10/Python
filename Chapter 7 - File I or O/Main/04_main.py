file_path = "Chapter 7 - File I or O/Main/file_name.txt"

# Basic version
file = open(file_path, "r")
print(file.read())
file.close()

# Recommended version using 'with' statement
with open(file_path, "r") as file:
    print(file.read())
