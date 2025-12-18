Value_List = ["Apple", "Orange", 4, 45.96, False, "Aman", "Shubham", 10+4j]

# Original list
print(f"Original list := {Value_List}")
print(f"====*====*====*====\n")

# Append a new element
Value_List.append("Prince")
print(f"After append('Prince') := {Value_List}\n")

# Insert an element at a specific index
Value_List.insert(2, "Preet")
print(f"After insert(2, 'Preet') := {Value_List}\n")

# Remove an element
Value_List.remove(False)  # Remove the first occurrence of False
print(f"After remove(False) := {Value_List}\n")

# Pop an element (removes by index)
popped_value = Value_List.pop(1)
print(f"After pop(1) := {Value_List}, Popped value := {popped_value}\n")

# Count occurrences of an element
count_apple = Value_List.count("Apple")
print(f"Count of 'Apple' in list := {count_apple}\n")

# Find index of an element
index_Aman = Value_List.index("Aman")
print(f"Index of 'Aman' := {index_Aman}\n")

# Sort the list (only strings in this case)
# Extract only string elements for sorting
string_elements = [x for x in Value_List if isinstance(x, str)]
string_elements.sort()
print(f"Sorted string elements := {string_elements}\n")

# Reverse the list
Value_List.reverse()
print(f"After reverse() := {Value_List}\n")

# Clear the list (uncomment to test)
# Value_List.clear()
# print(f"After clear() := {Value_List}\n")