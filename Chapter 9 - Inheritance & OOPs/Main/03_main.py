print("====*==== Encapsulation ====*=====\n")

# Encapsulation = Binding data + methods inside a class.
# Protected Attribute  -> _var   (Accessible inside class + subclasses)
# Private Attribute    -> __var  (Accessible ONLY inside class, name-mangled)

class Demo:
    def __init__(self):
        self._protected = 1045               # Protected attribute
        self.__private = "Aman Patidar"      # Private attribute (name-mangled)

    def show(self):
        # Accessing protected + private inside the class → Allowed
        print(f"Protected: {self._protected}")
        print(f"Private:   {self.__private}")

# Child class to show protected access
class Child(Demo):
    def display_protected(self):
        # Protected can be accessed in subclasses
        print(f"Accessing protected in child: {self._protected}")
        # Private CANNOT be accessed → would give error
        # print(self.__private)  # ❌

# Creating objects
D = Demo()
D.show(f"")

C = Child()
C.display_protected()

# Accessing private attribute outside the class → error:
# print(D.__private)  # ❌ AttributeError

# But private can be accessed using name-mangling (not recommended)
print(f"Accessing private using name-mangling: {D._Demo__private}")