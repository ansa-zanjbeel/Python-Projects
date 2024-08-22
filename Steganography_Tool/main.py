from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb

root = Tk()
root.title("Steganography Tool")
root.geometry("700x500+350+100")
root.resizable(False,False)
root.configure(bg="#2f4155")

def ShowImage():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                        title="select image",
                                        filetype=(("PNG file","*.png"),
                                        ("JPG file","*.jpg"),("ALL file",".txt")))
    img=Image.open(filename)
    img=ImageTk.PhotoImage(img)
    l.configure(image=img,width=250,height=250)
    l.image=img

def Hide():
    global secret
    message=text1.get(1.0,END)
    secret = lsb.hide(str(filename),message)

def Show():
    clear_message = lsb.reveal(filename)
    text1.delete(1.0,END)
    text1.insert(END, clear_message)

def Save():
    secret.save("hidden.png")


#icon
image_icon=PhotoImage(file="images/logo.jpg")
root.iconphoto(False,image_icon)

#logo
logo=PhotoImage(file="images/logo.png")
Label(root,image=logo,bg="#2f4155").place(x=10,y=0)

Label(root,text="STEGANOGRAPHY TOOL", bg="#2d4155", fg="white",font="arial 25 bold").place(x=100,y=20)

#firstframe
f1=Frame(root,bd=1,bg="black",width=340,height=280,relief=GROOVE)
f1.place(x=10,y=80)

l=Label(f1,bg="black")
l.place(x=40,y=10)

#secondframe
f2=Frame(root,bd=1,bg="white",width=340,height=280,relief=GROOVE)
f2.place(x=350,y=80)

text1=Text(f2,font="Robote 20",bg="white",fg="black",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=320,height=295)

s1=Scrollbar(f2)
s1.place(x=320,y=0,height=300)

s1.configure(command=text1.yview)
text1.configure(yscrollcommand=s1.set)

#thirdframe
f3=Frame(root,bd=1,bg="#2f4155",width=330,height=100,relief=GROOVE)
f3.place(x=10,y=370)

Button(f3,text="Open Image",width=10,height=2,font="arial 14 bold",command=ShowImage).place(x=20,y=30)
Button(f3,text="Save Image",width=10,height=2,font="arial 14 bold",command=Save).place(x=180,y=30)
Label(f3,text="PhotoFile/Image",bg="#2f4155",fg="yellow").place(x=37,y=5)

#forthframe
f4=Frame(root,bd=1,bg="#2f4155",width=330,height=100,relief=GROOVE)
f4.place(x=360,y=370)

Button(f4,text="Hide Text",width=10,height=2,font="arial 14 bold",command=Hide).place(x=20,y=30)
Button(f4,text="Show Text",width=10,height=2,font="arial 14 bold",command=Show).place(x=180,y=30)
Label(f4,text="PhotoFile/Image",bg="#2f4155",fg="yellow").place(x=37,y=5)


root.mainloop()
