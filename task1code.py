import turtle

polygon=turtle.Turtle()

polygon.shape("square")
polygon.pencolor("red")
polygon.speed(5)
polygon.screen().bgcolor("black")

num_poly=8
num_sides=8
side_length=70
angle1=135.0
angle=360/num_sides
for j in range (num_poly):
    for i in range(num_sides):
        polygon.forward(side_length)
        polygon.right(angle)
    polygon.left(angle1)
turtle.done()
