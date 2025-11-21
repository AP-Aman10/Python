def print_list(friends, idx=0):
    """Recursively print each friend's name with its index."""
    if idx == len(friends):
        return
    print(f"Friend at index {idx}:= {friends[idx]}")
    print_list(friends, idx + 1)

def get_integer(prompt):
    """Safely get an integer from the user."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

# Ask number of friends
n = get_integer("How many friends do you want to enter:= ")

friends = []

# Get friend names
for i in range(1, n + 1):
    name = input(f"Enter friend {i}:= ")
    friends.append(name)

# Print using recursion
print("\n--- Friend List ---")
print_list(friends)