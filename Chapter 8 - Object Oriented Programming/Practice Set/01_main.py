# create student class that takes name & marks of 5 Subject as arguments in constructor. Then Create a Method to print  the average.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks  # Dictionary of subject: marks

    def show_result(self):
        total = sum(self.marks.values())
        average = total / len(self.marks)
        print(f"\nStudent Name: {self.name}")
        print("Marks Obtained:")
        for subject, mark in self.marks.items():
            print(f"  {subject}: {mark}")
        print(f"\nTotal Marks: {total}")
        print(f"Average Marks: {average:.2f}")


# --- Taking user input ---
name = input("Enter student name: ")

subjects = ["Hindi", "English", "Maths", "Science", "Social Science"]
marks = {}

for subject in subjects:
    mark = float(input(f"Enter marks for {subject}: "))
    marks[subject] = mark

# Create Student object
student = Student(name, marks)

# Show total and average
student.show_result()