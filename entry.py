from tkinter import *

root=Tk()
root.geometry("600x400")

'''
variables in tkniter
IntVar, StringVar,BooleanVar

'''
username=Label(root, text="Username")
username.grid()
password=Label(root,text="Passowrd")
password.grid()

entry1value=StringVar()
entry2value=StringVar()

entry1=Entry(root, textvariable=entry1value)
entry1.grid(row=0, column=1)
entry2=Entry(root, textvariable=entry2value)
entry2.grid(row=1,column=1)

root.mainloop()