from tkinter import *

root=Tk()
root.geometry("500x500")

def display():
    print(nameval.get(),mobileval.get(),ageval.get(),schoolval.get())

name=Label(root, text="Name")
age=Label(root, text="Age")
mobile=Label(root, text="Mobile")
school=Label(root, text="School")

name.grid(row=1, column=2)
age.grid(row=2,column=2)
mobile.grid(row=3,column=2)
school.grid(row=4,column=2)

nameval=StringVar()
ageval=IntVar()
mobileval=StringVar()
schoolval=StringVar()

nameentry=Entry(root, textvariable=nameval)
ageentry=Entry(root, textvariable=ageval)
mobileentry=Entry(root, textvariable=mobileval)
schoolentry=Entry(root, textvariable=schoolval)

nameentry.grid(row=1, column=3)
ageentry.grid(row=2,column=3)
mobileentry.grid(row=3,column=3)
schoolentry.grid(row=4,column=3)

button=Button(root, text="Submit", command=display)
button.grid(row=5,column=3)
root.mainloop()