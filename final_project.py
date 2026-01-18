#for koch snowflake: axiom=F--F--F, rule= F--> F+F++F+F, angle=60,+=turn right,-=turn left
#for algae: Axiom=A, rule= A-->AB,B-->A
#for fractal plant: Axiom=X, rule= X --> F+[[X]-X]-F[-FX]+X, F --> FF

#CODE FOR KOCH SNOWFLAKE PATTERN:

import turtle
import tkinter as tk

#DEFINING SYMBOLS,AXIOMS AND RULES
axiom="F--F--F"
rules={"F" : "F+F--F+F"} # If we want another symbol like X, define its rule set in the dictionary, put another elif statement in draw function
iterations=3

def apply_rules(axiom, rules, iterations):
    current = axiom
    for _ in range(iterations):
        next_string = ""
        for ch in current:
            next_string += rules.get(ch, ch)
        current = next_string
    return current
lsys_string = apply_rules(axiom, rules, iterations)

stack = []

def draw(commands, length=15, angle=60):
    for i in commands:
        if i == 'F':      
            t.forward(length)
        elif i == '+':
            t.right(angle)
        elif i == '-':    
            t.left(angle)
        elif i == '[':    
            stack.append((t.position(), t.heading()))
        elif i == ']':    
            pos, head = stack.pop()
            t.penup()
            t.setposition(pos)
            t.setheading(head)
            t.pendown()

def generate_output():
    draw(lsys_string) 

#MAKE THE CANVAS AND THE INPUT DASHBOARD USING TKINTER

root=tk.Tk()
root.title("L-Systems")
root.geometry("800x800")

canvas=tk.Canvas(root,height=825,bg="white")
canvas.pack(fill="x",padx=5,pady=5)

button=tk.Button(root, text="Generate", command = generate_output)
button.pack(padx=5,pady=5)

label1=tk.Label(root,text="Axiom")
label1.pack(padx=5,pady=5)

entry1=tk.Entry(root)
entry1.pack(padx=5,pady=5)
entry1.insert(0, "Axiom: F--F--F")

label2=tk.Label(root,text="Rule Set")
label2.pack(padx=5,pady=5)

textbox=tk.Text(root, height=3)
textbox.pack(padx=5,pady=5)
textbox.insert("1.0", "F : F+F--F+F\n")
textbox.insert("2.0", "+ : Turn right by an angle\n")
textbox.insert("3.0", "- : Turn left by an angle")


label3=tk.Label(root,text="Iterations")
label3.pack(padx=5,pady=5)

entry2=tk.Entry(root)
entry2.pack(padx=5,pady=5)
entry2.insert(0, "Iterations : 3")

screen=turtle.TurtleScreen(canvas) #Tells turtle to use that areaiter
t=turtle.RawTurtle(canvas) #A turtle living inside that canvas

screen.bgcolor("white")
#TURTLE CUSOMTIZATION
t.shape("turtle")
t.pensize(5)
t.pencolor("red")
t.speed(0)


#POSITION TURTLE TO BOTTOM OF THE SCREEN
t.penup()
t.goto(740.0,-375.0)
t.left(90)
t.pendown()   

#TO ENSURE TURTLE DOESNT DRAW AFTER WINDOW CLOSES
def on_close():
    root.destroy()
root.protocol("WM_DELETE_WINDOW",on_close)

root.mainloop()

