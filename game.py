om turtle import *
import turtle as tur

wd=tur.Screen()
 
turt=tur.Turtle()
tur.title("Pythontpoint") 
turt.color("blue")
turt.width("4")
 
turt.speed(2)
 
for i in range(4):
    turt.forward(300)
    turt.left(90)

turt.penup()
turt.goto(0,100)
turt.pendown()

turt.forward(300)

turt.penup()
turt.goto(0,200)
turt.pendown()
 
turt.forward(300)
 
turt.penup()
turt.goto(100,0)
turt.pendown()

turt.forward(300)
 
turt.penup()
turt.goto(100,0)
turt.pendown()
 
turt.left(90)
turt.forward(300)
 
turt.penup()
turt.goto(200,0)
turt.pendown()
 
 
turt.forward(300)

tur.done()
