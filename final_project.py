import turtle
import tkinter as tk

#MAKE THE CANVAS AND THE INPUT DASHBOARD USING TKINTER

root=tk.Tk()
root.title("L-Systems")
root.geometry("800x800")

canvas=tk.Canvas(root,height=700,bg="white")
canvas.pack(fill="x",padx=10,pady=10)

button=tk.Button(root, text="Generate",command = generate_output)
button.pack(padx=10,pady=10)

label1=tk.Label(root,text="Axiom")
label1.pack(padx=10,pady=10)

entry1=tk.Entry(root)
entry1.pack(padx=10,pady=10)
entry1.insert(0, "Axiom: F")

label2=tk.Label(root,text="Rule Set")
label2.pack(padx=10,pady=10)

textbox=tk.Text(root, height=3)
textbox.pack(padx=10,pady=10)
textbox.insert("1.0", "F : F[-F][+F]\n")
textbox.insert("2.0", "+ : Turn right by an angle\n")
textbox.insert("3.0", "- : Turn left by an angle")


label3=tk.Label(root,text="Iterations")
label3.pack(padx=10,pady=10)

entry2=tk.Entry(root)
entry2.pack(padx=10,pady=10)
entry2.insert(0, "Iterations : 0")

screen=turtle.TurtleScreen(canvas) #Tells turtle to use that areaiter
t=turtle.RawTurtle(canvas) #A turtle living inside that canvas

screen.bgcolor("yellow")
#TURTLE CUSOMTIZATION
t.shape("turtle")
t.pensize(5)
t.pencolor("red")
t.speed(6)


#POSITION TURTLE TO BOTTOM OF THE SCREEN
t.penup()
t.goto(740.0,0)
t.left(90)
t.pendown()

#DEFINING SYMBOLS,AXIOMS AND RULES
axiom="F"
rules={"F" : "F[-F][+F]"}
iterations=4

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

def draw(commands, length=75, angle=67):
    for cmd in commands:
        if cmd == 'F':      
            t.forward(length)
        elif cmd == '+':
            t.right(angle)
        elif cmd == '-':    
            t.left(angle)
        elif cmd == '[':    
            stack.append((t.position(), t.heading()))
        elif cmd == ']':    
            pos, head = stack.pop()
            t.penup()
            t.setposition(pos)
            t.setheading(head)
            t.pendown()

def generate_output():
    draw(lsys_string)   

root.mainloop()

