class Table:
    def __init__(self, num):
        self.num = num
    
    def print_Table(self):
        for i in range(1, 10+1):
            print(f"{self.num} X {i} = {self.num * i}")
            
Num = int(input("Enter the Num:= "))
TB = Table(Num)
TB.print_Table()