# Dictionary of student marks
student = {
    "Name": "Aman Patidar",
    "Class": "XII",
    "Mobile No.": 9982325319,
    "Marks": {
        "Hindi": 92,
        "English": 89,
        "Maths": 99,
        "Science": 85,
        "SST": 95
    }
}

print(f"Type of Student:= {type(student)}")
print("====*====*====*====\n")

print(f"Name of Student:= {student.get('Name')}")
print(f"Class of Student:= {student.get('Class')}")
print(f"Mobile No. of Student:= {student.get('Mobile No.')}")
print("====*====*====*====\n")

for Subject, marks in student["Marks"].items():
    print(f"{Subject}:= {marks}")