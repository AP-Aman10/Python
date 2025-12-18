print("====*==== Access Specifiers in Python ====*=====\n")

class Student:
    def __init__(self):
        self.name = "Aman"        # Public attribute
        self._age = 20            # Protected attribute (convention-based)
        self.__marks = 95         # Private attribute (name mangling)

    # Public method to access private data
    def get_marks(self):
        return self.__marks


# Object creation
s = Student()

# Public: Accessible everywhere
print("Public Name: ", s.name)

# Protected: Accessible but NOT recommended outside class/subclass
print("Protected Age: ", s._age)

# Private: Not directly accessible → use getter method
print("Private Marks (via method): ", s.get_marks())

# Name-mangling: Not recommended but possible
print("Private Marks (name-mangling): ", s._Student__marks)
