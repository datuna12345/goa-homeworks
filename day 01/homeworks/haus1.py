from turtle import *


#we want to paint a haus

#step 1: draw a square
speed(30)
width(7)
color("brown")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#drawing a door

forward(70)
color("purple")
begin_fill()
left(90)
forward(125)     #height of the door
right(90)
forward(60)
right(90)
forward(125)
end_fill()

penup()
goto(200,200)
pendown()

color("blue")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


#drawing a window

penup()
goto(20,160)
pendown()

color("grey")
begin_fill()
left(30)
forward(40)
left(90)
forward(30)
left(90)
forward(40)
left(90)
forward(30)


penup()
goto(150,160)
pendown()

left(90)
forward(40)
left(90)
forward(30)
left(90)
forward(40)
left(90)
forward(30)
end_fill()


penup()
goto(95,367)
pendown()


color("red")
begin_fill()
forward(300)
left(90)
forward(170)
left(90)
forward(200)
end_fill()

begin_fill()
penup()
goto(-200,200)
pendown()


right(90)
forward(200)
left(90)
forward(200)
end_fill()



penup()
goto(-150,300)
pendown()



color("grey")
begin_fill()

forward(80)
right(90)
forward(40)
right(90)
forward(80)
right(90)
forward(40)
end_fill()



penup()
goto(-160,120)
pendown()

color("grey")
begin_fill()
forward(40)
right(90)
forward(30)
right(90)
forward(40)
right(90)
forward(30)


penup()
goto(-70,120)
pendown()


right(90)
forward(40)
right(90)
forward(30)
right(90)
forward(40)
right(90)
forward(30)
end_fill()


begin_fill()
penup()
goto(120,290)
pendown()


forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()
































exitonclick()