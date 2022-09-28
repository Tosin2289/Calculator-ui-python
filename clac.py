import tkinter
import sys
from tkinter import *

top=Tk()
top.title("Calculator")
top.geometry("400x600")

def exe():
    sys.exit()

e1=Entry(top,width=400,bd=2,font=("Times",25,"bold"),bg="grey",fg="white")
e1.pack(fill="both",expand="true")


frame=Frame(top,height=500,bg="black",width=400)
frame.pack()

b1=Button(frame,text="7",font=("Times",35,"bold"),bg="white",bd=8)
b1.place(x=2,y=5)

b2=Button(frame,text="8",font=("Times",35,"bold"),bg="white",bd=8)
b2.place(x=75,y=5)

b3=Button(frame,text="9",font=("Times",35,"bold"),bg="white",bd=8)
b3.place(x=150,y=5)

bplus=Button(frame,text="+",font=("Times",35,"bold"),bg="white",bd=8,padx=50)
bplus.place(x=225,y=5)

#==================================================================

b4=Button(frame,text="4",font=("Times",35,"bold"),bg="white",bd=8)
b4.place(x=2,y=105)

b5=Button(frame,text="5",font=("Times",35,"bold"),bg="white",bd=8)
b5.place(x=75,y=105)

b6=Button(frame,text="6",font=("Times",35,"bold"),bg="white",bd=8)
b6.place(x=150,y=105)

bminus=Button(frame,text="-",font=("Times",35,"bold"),bg="white",bd=8,padx=55)
bminus.place(x=225,y=105)

#===================================================================
b7=Button(frame,text="1",font=("Times",35,"bold"),bg="white",bd=8)
b7.place(x=2,y=205)

b8=Button(frame,text="2",font=("Times",35,"bold"),bg="white",bd=8)
b8.place(x=75,y=205)

b9=Button(frame,text="3",font=("Times",35,"bold"),bg="white",bd=8)
b9.place(x=150,y=205)

bmulti=Button(frame,text="x",font=("Times",35,"bold"),bg="white",bd=8,padx=51)
bmulti.place(x=225,y=205)

bdiv=Button(frame,text="/",font=("Times",33,"bold"),bg="white",bd=8,padx=58)
bdiv.place(x=225,y=305)

#============================================================================
bexe=Button(frame,text="E",font=("Times",35,"bold"),bg="red",bd=5,padx=30,command=exe)
bexe.place(x=90,y=305)

bcls=Button(frame,text="C",font=("Times",35,"bold"),bg="white",bd=5,padx=10)
bcls.place(x=2,y=305)

bequ=Button(frame,text="=",font=("Times",35,"bold"),bg="white",bd=5,padx=165,pady=2)
bequ.place(x=2,y=400)

top.mainloop()


