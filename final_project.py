import turtle
import tkinter as tk

#MAKE THE CANVAS AND THE INPUT DASHBOARD USING TKINTER

root=tk.Tk()
root.title("L-Systems")
root.geometry("800x800")

canvas=tk.Canvas(root,height=700,bg="white")
canvas.pack(fill="x",padx=10,pady=10)

button=tk.Button(root, text="Generate")
button.pack(padx=10,pady=10)

label1=tk.Label(root,text="Axiom")
label1.pack(padx=10,pady=10)

entry1=tk.Entry(root)
entry1.pack(padx=10,pady=10)

label2=tk.Label(root,text="Rule Set")
label2.pack(padx=10,pady=10)

textbox=tk.Text(root, height=3)
textbox.pack(padx=10,pady=10)

label3=tk.Label(root,text="Iterations")
label3.pack(padx=10,pady=10)

entry2=tk.Entry(root)
entry2.pack(padx=10,pady=10)

screen=turtle.TurtleScreen(canvas) #Tells turtle to use that area
t=turtle.RawTurtle(canvas) #A turtle living inside that canvas

screen.bgcolor("yellow")
#TURTLE CUSOMTIZATION
t.shape("turtle")
t.pensize(5)
t.pencolor("red")
t.speed(6)


#POSITION TURTLE TO BOTTOM OF THE SCREEN
t.penup()
t.goto(740.0,-340.0)
t.left(90)
t.pendown()

root.mainloop()

