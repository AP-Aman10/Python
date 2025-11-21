# Ask the user for words to censor, separated by commas
user_input = input("Enter words to censor, separated by commas: ")
words_to_censor = [word.strip() for word in user_input.split(",")]

file_path = "Chapter 7 - File I or O/Main/file_name.txt"

# Read the file content
with open(file_path, "r") as file:
    file_content = file.read()

# Replace each word with '#' characters
for word in words_to_censor:
    file_content = file_content.replace(word, "#" * len(word))

# Write the censored content back to the file
with open(file_path, "w") as file:
    file.write(file_content)

print(f"Censored {len(words_to_censor)} words in {file_path}.")
