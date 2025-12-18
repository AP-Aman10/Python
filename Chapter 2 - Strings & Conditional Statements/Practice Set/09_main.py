# Asking user to enter a post
user_post = input("Enter the post: ")

# Checking if the post mentions "harry"
if "aman" in user_post.lower():
    print("This post is talking about Aman.")
else:
    print("This post is not talking about Aman.")