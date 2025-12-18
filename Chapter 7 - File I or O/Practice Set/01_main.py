file_path = "Chapter 7 - File I or O/Practice Set/Poem.txt"

with open(file_path, "r") as file:
    content = file.read()

if "twinkle" in content:
    print("The word 'twinkle' is present in the content.")
else:
    print("The word 'twinkle' is not present in the content.")
