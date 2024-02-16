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

#wybór typu
print("wpisz 1 dla standardowej tęczy\n")
print("wpisz 2 dla tęczy z losowymi kolorami\n")
print("wpisz 3 dla tęczy z dodatkowymi kolorami\n")
choice = int(input("--> "))

t.pensize(pSize)

if(choice == 1):
    for i in range(len(colList)):
        step = ((math.pi * radius)/ 180)
        bow(radius, step, colList[i] )
        radius = radius + pSize

elif(choice == 2):
    print("nic sie nie dzieje, czekasz z emocjami na dzień w którym to nadejdzie")

elif(choice == 3):
    print("nic sie nie dzieje, każdy kolejny dzień oczekiwań wydaje sie dłuższy")

else:
    print("zły numer")