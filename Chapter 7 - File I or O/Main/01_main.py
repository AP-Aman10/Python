# Reading a file and storing its content
file_name = "Chapter 7 - File I or O/Main/file_name.txt"  # this is already a string

with open(file_name, "r") as file:  # just use the variable directly
    file_content = file.read()

# Print the file content
print("File Content:\n", file_content)

# Placeholder for emails (can be used later)
extracted_emails = []
