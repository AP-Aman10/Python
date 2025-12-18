print("====*==== Virtual Function (Polymorphism) ====*=====\n")

# Base Class
class Animal:
    # Acts like a virtual function (Python supports this automatically)
    def sound(self):
        print("Animal makes a sound")


# Derived Classes
class Dog(Animal):
    def sound(self):
        print("🐶 Dog barks")


class Cat(Animal):
    def sound(self):
        print("🐱 Cat meows")


class Cow(Animal):
    def sound(self):
        print("🐄 Cow moos")


class Lion(Animal):
    def sound(self):
        print("🦁 Lion roars")


# Function demonstrating runtime polymorphism
def make_sound(animal: Animal):
    """
    This function accepts ANY object of type Animal.
    At runtime, Python automatically calls the overridden method.
    """
    animal.sound()


# Using polymorphism
animals = [Cat(), Dog(), Cow(), Lion()]

for a in animals:
    make_sound(a)
