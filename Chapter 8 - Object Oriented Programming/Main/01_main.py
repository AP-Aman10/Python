class Student:
    Collage_Name = "Knight Collage"
    # default Constructors
    def __init__(self):
        pass

    # Parameterized Constructors
    def __init__(self, Name, Marks):
        self.name = Name
        self.marks = Marks
    
    def Welcome(self):
        print("Welcome Student")

print(f"Collage Name:= {Student.Collage_Name}")
S1 = Student("Aman Patidar", 98)
print(f"Hey, {S1.name}! 🎈 You're Marks is {S1.marks}!")
S1.Welcome()
print("====*====*====*====\n")

print(f"Collage Name:= {Student.Collage_Name}")
S1 = Student("Shubham Patidar", 94)
print(f"Hey, {S1.name}! 🎈 You're Marks is {S1.marks}!")
S1.Welcome()
print("====*====*====*====\n")