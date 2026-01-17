import turtle

wn=turtle.Screen()
wn.bgcolor("white")
wn.title("My turtle window!!")

polygon=turtle.Turtle()

polygon.shape("turtle")
polygon.pencolor(0.4,0.8,0.1)
polygon.speed(5)
polygon.pensize(5)

num_poly=8
num_sides=8
side_length=70
angle1=135.0
angle=360/num_sides
polygon.penup()
polygon.goto(0,250)
polygon.pendown()
for j in range (num_poly):
    for i in range(num_sides):
        polygon.forward(side_length)
        polygon.right(angle)
    polygon.left(angle1)
print(polygon.xcor(),polygon.ycor())
polygon.penup()
polygon.goto(20,20)
polygon.pendown()

polygon.forward(75)
polygon.left(45)
polygon.forward(75)
polygon.right(90)
polygon.forward(75)
polygon.left(45)
polygon.forward(75)
polygon.penup()
polygon.home()
polygon.pendown()
polygon.circle(25)
polygon.penup()
polygon.backward(75)
polygon.pendown()

polygon.begin_fill()
for _ in range(4):
    polygon.forward(100)
    polygon.right(90)
polygon.end_fill
polygon.fillcolor("yellow")


turtle.done()
