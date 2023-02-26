from tkinter import *
import time

root=Tk()
root.geometry("600x400")

def func():
    svalue.set("Busy....")
    time.sleep(2)
    svalue.set("Uploading...")

svalue=StringVar()

l1=Label(root, textvariable=svalue,relief=SUNKEN,anchor="w")
l1.pack(side=BOTTOM,fill="x",pady=40)

b1=Button(root, text="Submit",command=func).pack()

root.mainloop()