print("====*==== Classes & Objects ====*=====\n")

# Class:= A class is a blueprint for creating objects.
# Object:= An object is an instance of a class.

class Car:   # Class
    def __init__(self, brand, color):
        # Instance attributes
        self.brand = brand
        self.color = color

    def start(self):
        # Method to start the car
        print(f"{self.color} {self.brand} car has started.")

# Creating an object (instance of Car)
my_car = Car("BMW", "Black")

# Calling object method
my_car.start()