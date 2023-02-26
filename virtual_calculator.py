from tkinter import *

root=Tk()
root.geometry("600x550")
root.title("Virtual Calculator")
root.configure(background="cyan")

def click(event):
    global svalue
    text=event.widget.cget("text")
    
    if text=="=":
        if svalue.get().isdigit():
            value=int(svalue.get())
        else:
            try:
                value=eval(svalue.get())
            except exception as e:
                print(e)
                value="error"
        svalue.set(value)
        screen.update()
    elif text=="C":
        svalue.set("")
        screen.update()
    else:
        svalue.set(svalue.get()+text)
        screen.update()
        

svalue=StringVar()

screen=Entry(root, textvariable=svalue, font="lucina 30 bold")
screen.pack(padx=10,pady=20)

f1=Frame(root, bg="grey",bd=6)
f1.pack()

b1=Button(f1, text="1",padx=10,pady=5)
b1.pack(side=LEFT,padx=10)
b1.bind('<Button-1>', click)
b2=Button(f1, text="2",padx=10,pady=5)
b2.pack(side=LEFT,padx=10)
b2.bind('<Button-1>', click)
b3=Button(f1, text="3",padx=10,pady=5)
b3.pack(side=LEFT,padx=10)
b3.bind('<Button-1>', click)
b4=Button(f1, text="4",padx=10,pady=5)
b4.pack(side=LEFT,padx=10)
b4.bind('<Button-1>', click)

f2=Frame(root, bg="grey",bd=6)
f2.pack()

b1=Button(f2, text="5",padx=10,pady=5)
b1.pack(side=LEFT,padx=10)
b1.bind('<Button-1>', click)
b2=Button(f2, text="6",padx=10,pady=5)
b2.pack(side=LEFT,padx=10)
b2.bind('<Button-1>', click)
b3=Button(f2, text="7",padx=10,pady=5)
b3.pack(side=LEFT,padx=10)
b3.bind('<Button-1>', click)
b4=Button(f2, text="8",padx=10,pady=5)
b4.pack(side=LEFT,padx=10)
b4.bind('<Button-1>', click)

f3=Frame(root, bg="grey",bd=6)
f3.pack()

b1=Button(f3, text="+",padx=10,pady=5)
b1.pack(side=LEFT,padx=10)
b1.bind('<Button-1>', click)
b2=Button(f3, text="9",padx=10,pady=5)
b2.pack(side=LEFT,padx=10)
b2.bind('<Button-1>', click)
b3=Button(f3, text="0",padx=10,pady=5)
b3.pack(side=LEFT,padx=10)
b3.bind('<Button-1>', click)
b4=Button(f3, text="*",padx=10,pady=5)
b4.pack(side=LEFT,padx=10)
b4.bind('<Button-1>', click)

f4=Frame(root, bg="grey",bd=6)
f4.pack()

b1=Button(f4, text="C",padx=10,pady=5)
b1.pack(side=LEFT,padx=10)
b1.bind('<Button-1>', click)
b2=Button(f4, text="-",padx=10,pady=5)
b2.pack(side=LEFT,padx=10)
b2.bind('<Button-1>', click)
b3=Button(f4, text="/",padx=10,pady=5)
b3.pack(side=LEFT,padx=10)
b3.bind('<Button-1>', click)
b4=Button(f4, text="=",padx=10,pady=5)
b4.pack(side=LEFT,padx=10)
b4.bind('<Button-1>', click)

root.mainloop()