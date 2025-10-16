source_file = "File I or O/file_name.txt"
copy_file = "File I or O/Practice Set/this_copy.txt"

# Read content from the source file
with open(source_file, "r") as file1:
    source_content = file1.read()

# Read content from the copy file
with open(copy_file, "r") as file2:
    copy_content = file2.read()

# Compare the contents
if source_content == copy_content:
    print("Yes, these files are identical.")
else:
    print("No, these files are not identical.")
