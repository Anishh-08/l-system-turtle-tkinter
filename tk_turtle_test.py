import tkinter as tk
root=tk.Tk()
root.title("My first GUI")
root.geometry("500x500")

label=tk.Label(root, text="Exploring GUI")
label.pack(padx=10,pady=10)

textbox=tk.Text(root,height=4)
textbox.pack(padx=10,pady=10)

entry=tk.Entry(root)
entry.pack(padx=10,pady=10)

button=tk.Button(root, text="Generate")
button.pack(padx=10,pady=10)

canvas=tk.Canvas(root,height=500,bg="white")
canvas.pack(fill="x",padx=10,pady=10)

root.mainloop()

