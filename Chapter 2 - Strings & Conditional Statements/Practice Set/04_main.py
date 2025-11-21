# Asking user for marks in four subjects
marks_subject1 = int(input("Enter marks for Subject 1: "))
marks_subject2 = int(input("Enter marks for Subject 2: "))
marks_subject3 = int(input("Enter marks for Subject 3: "))
marks_subject4 = int(input("Enter marks for Subject 4: "))

# Calculating total percentage
total_percentage = (marks_subject1 + marks_subject2 + marks_subject3 + marks_subject4) / 4

# Checking pass/fail criteria
if (total_percentage >= 40 and 
    marks_subject1 >= 33 and 
    marks_subject2 >= 33 and 
    marks_subject3 >= 33 and 
    marks_subject4 >= 33):
    print(f"Congratulations! You passed with {total_percentage:.2f}%")
else:
    print(f"Sorry, you failed. Your percentage is {total_percentage:.2f}%")

print("End of Program")
