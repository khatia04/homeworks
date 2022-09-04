from turtle import *



# we want to paint a house 
# step1: draw a square

width(3)
color("green")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door 
begin_fill()
forward(70)
color("blue")
left(90)
forward(120) #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()
# end of the door 

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
# end of the roof 

#step4: draw a window
color("green")
left(208)

pendown()
penup()
backward(30)
goto(10, 120)


#draw  window 1
width(9)
color ("brown")
begin_fill()
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
end_fill()

#draw window 2 
goto( 140,120)
begin_fill()
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
end_fill()












exitonclick() 














