file_path = "File I or O/file_name.txt"

# Open the file and read line by line
with open(file_path, "r") as file:
    current_line = file.readline()
    while current_line != "":
        print(current_line, end="")  # end="" avoids extra newlines
        current_line = file.readline()
