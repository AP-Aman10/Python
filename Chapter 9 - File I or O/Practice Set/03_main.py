file_path = "File I or O/file_name.txt"

with open(file_path, "r") as file:
    log_content = file.read()

if "Aman" in log_content:
    print("Yes, 'Aman' is present in the file.")
else:
    print("No, 'Aman' is not present in the file.")
