class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y

# Calling the static method directly from the class
print(MathUtils.add(4, 96))

# Calling it through an instance
obj = MathUtils()
print(obj.add(4,96))
