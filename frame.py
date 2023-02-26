from tkinter import *

root=Tk()
root.geometry("600x400")

f1=Frame(root, bg="grey", bd=6, relief=SUNKEN,pady=50)
f1.pack(side=BOTTOM,fill="x")

f2=Frame(root, bg="grey", bd=6, relief=SUNKEN,padx=50)
f2.pack(side=LEFT,fill="y")

l1=Label(f1, text="Files")
l1.pack(side=LEFT)

l2=Label(f2, text="Shell")
l2.pack()

root.mainloop()
