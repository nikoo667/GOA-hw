from turtle import *
#we want to draw a house

# drawing a square

speed(20)
width(7)
color("blue")
forward (200)
left (90)

forward(200)
left(90)

forward (200)
left (90)

forward(200)
left(90)
#end of the square

#drawing the door

forward (70)
color("blue")
left(90)
forward(100) #height of the door
right(90)

forward(60)
right (90)

forward(100)

penup()
goto(200,200)
pendown()

color("yellow")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#drawing windows
penup()
goto()
pendown()
