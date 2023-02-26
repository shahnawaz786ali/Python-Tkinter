from tkinter import *

root=Tk()
root.geometry("600x400")
root.title("Handling Events")
root.configure(background="green")

def click(event):
    print("Handling events")
    print(f"Coordinate points:({event.x}, {event.y})")

b1=Button(root, text="Click me please",pady=10)
b1.pack()
b1.bind("<Button-1>",click)
b1.bind("<Double-1>",exit)

root.mainloop()