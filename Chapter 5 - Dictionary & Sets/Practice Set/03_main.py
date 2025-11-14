# Dictionary to store friends and their preferred languages
friends_languages = {}

# Asking for friends' names and their languages
friend_name1 = input("Enter friend's name: ")
language1 = input("Enter language they speak: ")
friends_languages.update({friend_name1: language1})

friend_name2 = input("Enter friend's name: ")
language2 = input("Enter language they speak: ")
friends_languages.update({friend_name2: language2})

friend_name3 = input("Enter friend's name: ")
language3 = input("Enter language they speak: ")
friends_languages.update({friend_name3: language3})

friend_name4 = input("Enter friend's name: ")
language4 = input("Enter language they speak: ")
friends_languages.update({friend_name4: language4})

print("Friends and their languages:", friends_languages)
