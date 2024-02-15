import turtle as t
import math

#rysuje łuk tęczy
def bow(r, s, c):
    t.speed(1000)
    t.penup()
    t.goto(-r,0)
    t.setheading(90)
    t.pendown()
    t.color(c)
    for i in range(0,180):
        t.forward(s)
        t.right(1)

#standardowe kolory
colList = ['purple', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red',]
#wybór wielkości
radius = int(input("jaki promień ma mieć tęcza?: "))
pSize = radius / 10
step = ((math.pi * radius )/ 180)
"""
#wybór typu
print("wpisz 1 dla standardowej tęczy\n")
print("wpisz 2 dla tęczy z losowymi kolorami\n")
print("wpisz 3 dla tęczy z dodatkowymi kolorami\n")
choice = int(input("--> "))
"""
choice = 1
t.pensize(pSize)

if(choice == 1):
    for i in range(len(colList)):
        bow(radius, step, colList[i] )
        radius = radius + pSize
        step = ((math.pi * radius)/ 180)

