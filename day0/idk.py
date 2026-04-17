from turtle import *

#house
speed(6.7)
width(6.7)
color("blue")
forward(300)
left(90)
forward(300)
left(90)
forward(300)
left(90)
forward(300)
#squareend

#door
left(90)
forward(120)
begin_fill()    
color("brown")
left(90)
forward(150)
right(90)
forward(75)
right(90)
forward(150)
end_fill()
#doorend

#roof
penup()
goto(300,300)
pendown()
shape("turtle")
color("red")
begin_fill()    
right(150)
forward(300)
left(120)
forward(300)
end_fill()  
#roofend

#window1
penup()
goto(40,150)
pendown()
color("yellow")
begin_fill()
left(120)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

#window2
penup()
goto(215,150)
pendown()
color("yellow")
begin_fill()
left(90)    
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()
hideturtle()

exitonclick()
