source_file = "Chapter 7 - File I or O/Main/file_name.txt"
destination_file = "Chapter 7 - File I or O/Practice Set/this_copy.txt"

# Read content from the source file
with open(source_file, "r") as src:
    file_content = src.read()

# Write content to the destination file
with open(destination_file, "w") as dest:
    dest.write(file_content)

print(f"Copied content from {source_file} to {destination_file}.")
