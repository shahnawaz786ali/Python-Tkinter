from tkinter import *

root=Tk()
root.geometry("600x400")
root.title("Menus and Submenus")
root.configure(background="yellow")

def display():
    print("Hello")

mainmenu=Menu(root)
m1=Menu(mainmenu,tearoff=0)
m1.add_command(label="New File",command=display)
m1.add_cascade(label="Open File")

m2=Menu(mainmenu,tearoff=0)
m2.add_command(label="Cut")
m2.add_command(label="Copy")
m2.add_separator()
m2.add_command(label="Paste")

m3=Menu(mainmenu,tearoff=0)

root.configure(menu=mainmenu)

mainmenu.add_cascade(label="File",menu=m1)
mainmenu.add_cascade(label="Edit",menu=m2)
mainmenu.add_cascade(label="Tools",menu=m3)

root.mainloop()