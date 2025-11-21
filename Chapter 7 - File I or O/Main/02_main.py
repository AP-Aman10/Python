# The text to write
credentials_text = "Email => amanpatidar812@gmail.com\nPassword => KnightR@10\n"

# File path
file_path = "Chapter 7 - File I or O/Main/myfile.txt"

# Make sure the folder exists manually before running, or create it yourself

# Open the file and write the content
with open(file_path, "w") as file:
    file.write(credentials_text)

print(f"Credentials have been saved to {file_path}")
