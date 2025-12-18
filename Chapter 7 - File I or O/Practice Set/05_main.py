print("====*==== 🔍 Word Find Code ====*====\n")

def check_for_word(filepath, word):
    """Check if the word exists anywhere in the file."""
    try:
        with open(filepath, "r") as file:
            data = file.read()
            if word in data:
                print("Found in file")
            else:
                print("Not Found")
    except FileNotFoundError:
        print("File not found!")


def check_for_line(filepath, word):
    """Return the line number where the word first appears."""
    try:
        with open(filepath, "r") as file:
            for line_no, line in enumerate(file, start=1):
                if word in line:
                    print(f"Found at line:= {line_no}")
                    return
        print("-1")  # Word not found
    except FileNotFoundError:
        print("File not found!")


# ---------- MAIN ---------
filepath = "Chapter 7 - File I or O/Practice Set/this_copy.txt"
search_word = input("Enter the word to search:= ")

check_for_word(filepath, search_word)
check_for_line(filepath, search_word)