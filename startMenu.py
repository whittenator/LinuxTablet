#!/usr/bin/python3
#simple GUI

import tkinter
import subprocess
import os
from tkinter import *

#Create the window
root = tkinter.Tk()

def developCallBack():
     subprocess.Popen("lxterminal")
    
   
   

#Modify root window
root.title("Linux Tablet Project")
root.geometry("800x480")

app = Frame(root,width=800,height=480)
app.pack(side=TOP)


#Linux Mode
button1 = Button(app, text = "Linux Mode", fg="red")
button1.grid(row=0,column=1,pady=70)


#Develop Mode
developBtn = Button(app, text = "Develop Mode", fg="green", command = developCallBack)
developBtn.grid(row=1,column=1,pady=70)

#Play Mode
playBtn = Button(app, text = "Play Mode", fg="orange")
playBtn.grid(row=2,column=1,pady=70)


#Kick off the event loop
root.mainloop()
