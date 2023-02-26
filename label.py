import tkinter

root=tkinter.Tk()
root.geometry("600x400")

f1=tkinter.Frame(root, bg="cyan", bd=4, relief=tkinter.SUNKEN)
f1.pack(side=tkinter.RIGHT,fill="y")

l1=tkinter.Label(f1,text="Label1")
l1.pack()

root.mainloop()