BLACK = "\033[30m"
RED = "\033[31m"
CYAN = "\033[36m"
RESET = "\033[0m"
print("====*==== Abstraction ====*=====\n")

from abc import ABC, abstractmethod

# Abstract class → defines common rules for all animals
class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def move(self):
        pass


# Animal class
class Animal(Animal):
    def sound(self):
        print(f"Animal barks 🦣")

    def move(self):
        print(f"Animal runs on four legs")


# Bird class
class Bird(Animal):
    def sound(self):
        print(f"Bird chirps 🐦‍🔥")

    def move(self):
        print(f"{RED}Bird flies in the sky")


# Fish class
class Fish(Animal):
    def sound(self):
        print(f"{RED}Fish does not make audible sound underwater 🦑{RESET}")

    def move(self):
        print(f"Fish swims in water")


# Using abstraction
animals = [Animal(), Bird(), Fish()]

for a in animals:
    a.sound()
    a.move()
    print()
