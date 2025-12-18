# Dictionary of words and their meanings
dictionary = {
    "madad": "Help",
    "kursi": "Chair",
    "billi": "Cat",
    "kitab": "Book",
    "paani": "Water",
    "ghar": "House",
    "dost": "Friend",
    "khushi": "Happiness",
    "safar": "Journey",
    "shanti": "Peace",
    "roti": "Bread",
    "gaadi": "Car",
    "taare": "Stars",
    "zameen": "Earth",
    "aakash": "Sky"
}

# Asking user for a word
user_word = input("Enter the word you want the meaning of: ").strip()

# Safely getting the meaning
meaning = dictionary.get(user_word, "Word not found in dictionary")

print(f"The meaning of '{user_word}' is: {meaning}")
