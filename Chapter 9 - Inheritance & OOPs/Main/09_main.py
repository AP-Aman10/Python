class Factorial:
    def __init__(self, num):
        self.num = num
    
    def Print_Fact(self):
        Fact = 1
        for i in range(1, self.num+1):
            Fact = Fact * i
        return Fact

Num = int(input("Enter the Num:= "))

FT = Factorial(Num)
print(f"Factorial of {Num}:= {FT.Print_Fact()}")