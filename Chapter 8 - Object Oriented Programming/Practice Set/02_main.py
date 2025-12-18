class Person:
    def __init__(self, Name, Age):
        self.name = Name
        self.age = Age
        
    @staticmethod
    def Mahadev():
        print("Har Har Mahadev")
    
P1 = Person("Aman Patidar", 19)
print(f"Hello! {P1.name} Your are {P1.age} Years Old")
P1.Mahadev()