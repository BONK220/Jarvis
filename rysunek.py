import turtle
import sys
from sys import exit

#zmienne turtla

bagno = turtle.Turtle()

#koniec zmiennych turtla


#rysunek
bagno.color("red","yellow")

bagno.begin_fill()

bagno.forward(100)
bagno.left(90)
bagno.forward(100)
bagno.left(90)
bagno.forward(100)
bagno.left(90)
bagno.forward(100)

bagno.end_fill()

bagno.color("yellow","red")

bagno.begin_fill()

bagno.right(90)
bagno.forward(300)
bagno.right(90)
bagno.forward(100)
bagno.right(90)
bagno.forward(300)

bagno.end_fill()

bagno.penup()
bagno.forward(200)
bagno.pendown()

bagno.color("red","yellow")

bagno.begin_fill()

bagno.forward(100)
bagno.right(90)
bagno.forward(100)
bagno.right(90)
bagno.forward(100)
bagno.right(90)
bagno.forward(100)
bagno.right(180)

bagno.end_fill()

bagno.penup()
bagno.forward(100)
bagno.pendown()

bagno.color("yellow","red")

bagno.begin_fill()

bagno.forward(300)
bagno.left(90)
bagno.forward(100)
bagno.left(90)
bagno.forward(300)

bagno.end_fill()

exit(0)


#koniec rysunku