# The text to write
credentials_text = "Email => amanpatidar812@gmail.com\nPassword => KnightP@10\n"

# File path
file_path = "File I or O/myfile.txt"

# Make sure the folder exists manually before running, or create it yourself

# Open the file and write the content
with open(file_path, "w") as file:
    file.write(credentials_text)

print(f"Credentials have been saved to {file_path}")
