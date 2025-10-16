# Mixed-type list
Value_List = ["Apple", "Orange", 4, 45.96, False, "Aman", "Shubham"]
print(f"Original Value_List: {Value_List}")

# Adding an element to the end of the list
Value_List.append("Prabhat")
print(f"After appending 'Prabhat': {Value_List}")

# Numeric list
Num_list = [1, 34, 62, 2, 6, 11]

# Removing element at index 3 and returning it
value = Num_list.pop(3)
print(f"Popped value at index 3: {value}")
print(f"List after popping: {Num_list}")
