print("====*==== Function Overriding ====*=====\n")

class Parent:
    # Method that will be overridden
    def show(self):
        print("Parent: Show Method")


class Child(Parent):
    # Overriding Parent's method
    def show(self):
        print("Child: Overridden Show Method")
        super().show()   # Optional: Access Parent's method


# Creating Child object
child = Child()
child.show()