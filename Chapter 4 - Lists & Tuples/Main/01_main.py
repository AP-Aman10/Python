Value_List = ["Apple", "Orange", 4, 45.96, False, "Aman", "Shubham"]

# Accessing the first element
print(f"Original first element: {Value_List[0]}")

# Changing the first element (lists are mutable)
Value_List[0] = "Grapes"
print(f"Updated first element: {Value_List[0]}")

# Slicing elements from index 1 to 3 (4 is excluded)
print(f"Sliced elements (index 1 to 3): {Value_List[1:4]}")

# Printing the whole list using f-string
print(f"Complete Value List: {Value_List}")