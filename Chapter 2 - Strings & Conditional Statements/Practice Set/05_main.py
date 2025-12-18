# List of spam phrases
spam_phrases = [
    "Make a lot of money",
    "buy now",
    "subscribe this",
    "click this"
]

# Asking user for a comment
user_comment = input("Enter your comment: ")

# Checking if the comment contains any spam phrases
if any(phrase in user_comment for phrase in spam_phrases):
    print("This comment is spam.")
else:
    print("This comment is not spam.")