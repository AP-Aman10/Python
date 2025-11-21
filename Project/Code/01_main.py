import math
from turtle import *

def hearta(k):
    return 15 *\
        math.sin(k)**3

def heartb(k):
    return 12 *\
        math.cos(k) - 5 *\
            math.cos(2*k) - 2 *\
                math.cos(3*k) -\
                    math.cos(4*k)

speed(0)
bgcolor("Black")
penup()
goto(0, 0)
pendown()
color("Red")

# Draw heart
for i in range(0, 4000):
    x = hearta(i) * 20
    y = heartb(i) * 20
    goto(x, y)

penup()
goto(0, -100)
color("Blue")
write("AP", align="center", font=("Arial", 100, "bold"))

done()