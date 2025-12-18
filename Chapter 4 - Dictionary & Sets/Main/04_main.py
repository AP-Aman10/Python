# Creating a set of numbers (duplicates are automatically removed)
number_set = {2, 4, 10, 20, 45, 47, 64, 81, 96, 100, 4, 4, 4, 4}
print(f"Initial number_set: {number_set}, Type: {type(number_set)}")

# Adding a new element to the set
number_set.add(566)
print(f"After adding 566: {number_set}, Type: {type(number_set)}")

# Removing an element safely
element_to_remove = 1
if element_to_remove in number_set:
    number_set.remove(element_to_remove)
    print(f"After removing {element_to_remove}: {number_set}, Type: {type(number_set)}")
else:
    print(f"Cannot remove {element_to_remove}: Not found in the set")
