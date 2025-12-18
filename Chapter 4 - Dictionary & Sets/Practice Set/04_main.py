# Creating a set of unique values
unique_values = set()

unique_values.add(20)    # integer
unique_values.add(20.0)  # float (duplicate of 20, won't be added)
unique_values.add('20')  # string (different from integer 20, will be added)

print(f"The unique values in the set are: {unique_values}")
print(f"The number of unique elements is: {len(unique_values)}")
