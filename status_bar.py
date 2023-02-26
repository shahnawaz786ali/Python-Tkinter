from tkinter import *

root=Tk()
root.geometry("600x500")
root.title("Status bar Widget")

label=Label(root, text="Uploading.....", bd=2, relief=SUNKEN, anchor=W, pady=20)
label.pack(side=BOTTOM, fill=X)

root.mainloop()