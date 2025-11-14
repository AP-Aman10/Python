# Creating a tuple with mixed data types
Value_Tuple = (4, 45.96, "Aman Patidar", 10 + 81j, True)
print(f"Value_Tuple: {Value_Tuple}")

# Counting how many times True appears in the tuple
no = Value_Tuple.count(True)
print(f"Number of times True appears: {no}")

# Finding the index of 45.96 in the tuple
i = Value_Tuple.index(45.96)
print(f"Index of 45.96: {i}")

# Length of the tuple
print(f"Length of Value_Tuple: {len(Value_Tuple)}")