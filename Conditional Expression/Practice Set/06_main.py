# Asking user for their marks
student_marks = int(input("Enter your marks (0-100): "))

# Determining grade based on marks
if 90 <= student_marks <= 100:
    grade = "A+"
elif 80 <= student_marks < 90:
    grade = "A"
elif 70 <= student_marks < 80:
    grade = "B"
elif 60 <= student_marks < 70:
    grade = "C"
elif 50 <= student_marks < 60:
    grade = "D"
elif 0 <= student_marks < 50:
    grade = "F"
else:
    grade = "Invalid marks"

print(f"Your grade is: {grade}")
