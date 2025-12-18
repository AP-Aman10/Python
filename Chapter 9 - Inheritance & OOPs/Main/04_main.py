print("====*==== Inheritance ====*=====\n")

# Parent Class (Base Class)
class Parent:
    def __init__(self):
        self.parent_name = "I am Parent Class 🤱"

    def show_parent(self):
        print("Parent Method Called")
        print(f"Message: {self.parent_name}")


# Child Class (Derived Class)
class Child(Parent):     # Inheriting Parent
    def __init__(self):
        super().__init__()     # Calling Parent constructor
        self.child_name = "I am Child Class 👦 "

    def show_child(self):
        print("Child Method Called")
        print(f"Message: {self.child_name}")


# Object of Child can access both Parent and Child methods
c = Child()
c.show_parent()   # Inherited from Parent
c.show_child()    # Defined in Child