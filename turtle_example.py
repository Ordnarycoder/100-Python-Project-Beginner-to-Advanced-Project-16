import turtle
import time
wn = turtle.Screen()
wn.bgcolor("red")
wn.title("Turtle Example")
skk = turtle.Turtle()
skk.pencolor("yellow")
i=0
while i <= 3:
    skk.forward(100)
    skk.left(90)
    i+=1
skk.penup()        
skk.goto(-120, -120)   
skk.pendown() 
a=0  
while a<36:
    skk.forward(200)
    skk.left(170)
    a +=1
r = 100
skk.penup()        
skk.goto(-180, 120)   
skk.pendown() 
skk.circle(r)
turtle.done()