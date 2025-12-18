class Cat:
    def sound(self):
        return "Cat Sound:= Meow 🐱"
    
class Cow:
    def sound(self):
        return "Cow Sound:= Moo 🐮"
    
class Dog:
    def sound(self):
        return "Dog Sound:= Bark 🐶"

class lion:
    def sound(self):
        return "Lion Sound:= Roar 🦁"
    
animals = [Cat(), Cow(), Dog(), lion()]

# Polymorphism in action
for animal in animals:
    print(animal.sound())
