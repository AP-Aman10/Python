class Person:
    def __init__(self, name, dob, gender, address):
        self.name = name
        self.dob = dob
        self.gender = gender
        self.address = address

    def display_info(self):
        print("\n--- Person Details ---")
        print(f"Name: {self.name}")
        print(f"Date of Birth: {self.dob}")
        print(f"Gender: {self.gender}")
        print(f"Address: {self.address}")

# Ask how many persons
num = int(input("How many persons do you want to enter? "))

# Create a list to store persons
persons = []

# Loop for each person
for i in range(num):
    print(f"\nEnter details for person {i+1}:")
    name = input("Enter your name: ")
    dob = input("Enter your Date of Birth (DD-MM-YYYY): ")
    gender = input("Enter your gender: ")
    address = input("Enter your address: ")
    persons.append(Person(name, dob, gender, address))

# Display all persons
print("\n========== All Persons ==========")
for p in persons:
    p.display_info()