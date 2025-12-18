print("====*==== Constructors & Destructors ====*=====\n") 

# Constructor (__init__):= Runs automatically when an object is created.
# Destructor (__del__):=  Runs when an object is destroyed (not commonly used).

class Person:
    def __init__(self, name):
        print("Constructor called")
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}.")

    def __del__(self):
        print("Destructor called")

# Creating object
P1 = Person("Aman")
P1.greet()

# Deleting object manually (forces destructor to run)
del P1