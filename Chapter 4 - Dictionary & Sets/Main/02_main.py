# Dictionary of student marks
student_marks = {
    "Aman": 100,
    "Shubham": 56,
    "Preet": 23,
    "Prince": 79
}

# Using .get() returns None if the key doesn't exist
print(f"Marks of Student2 using get(): {student_marks.get('Student2')}")

# Direct access using [] will raise a KeyError if the key doesn't exist
try:
    print(f"Marks of Student2 using []: {student_marks['Student2']}")
except KeyError:
    print("Error: 'Student2' does not exist in the dictionary")
