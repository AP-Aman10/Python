# Base class
class IndiaSymbol:
    def description(self):
        print("This is an important national symbol of India 🇮🇳")

# Derived classes
class NationalAnimal(IndiaSymbol):
    def name(self):
        print("National Animal of India: Bengal Tiger 🐅")
        print("====*====*====*====\n")

class NationalBird(IndiaSymbol):
    def name(self):
        print("National Bird of India: Indian Peacock 🦚")
        print("====*====*====*====\n")

class NationalFlag(IndiaSymbol):
    def name(self):
        print("National Flag of India: Tricolor 🇮🇳")
        print("====*====*====*====\n")

class NationalFlower(IndiaSymbol):
    def name(self):
        print("National Flower of India: Lotus 🌸")
        print("====*====*====*====\n")

# Using the classes
symbols = [NationalAnimal(), NationalBird(), NationalFlag(), NationalFlower()]

for symbol in symbols:
    symbol.description()
    symbol.name()