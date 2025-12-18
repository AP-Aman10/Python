value_list = ["Apple", "Orange", 4, 45.96, False, "Aman", "Shubham", 10+4j]

print("===== LIST DETAILS =====\n")
print(f"Original List: {value_list}")
print(f"Type of value_list: {type(value_list)}")
print(f"Length of list: {len(value_list)}")
print("\n====*====*====*====\n")

print("===== ELEMENT DETAILS =====")
for index, item in enumerate(value_list):
    print(f"Index {index}: Value = {item}, Type = {type(item)}")
