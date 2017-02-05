#!/usr/bin/python3
#simple GUI

import tkinter
import subprocess
import time
from tkinter import *

#Create the window
root = tkinter.Tk()

#Button Images
devPhoto = PhotoImage(file="devPic.png")
linPhoto = PhotoImage(file="linPic.png")
playPhoto = PhotoImage(file="playPic.png")

def developCallBack():
     subprocess.Popen(['lxterminal','--working-directory=/usr/local/bin'])
     
   
   

#Modify root window
root.title("Linux Tablet Project")
root.geometry("800x480")
root.resizable(False, False)

app = Frame(root,width=800,height=480)
app.pack(side=TOP)


#Linux Mode
button1 = Button(app, text = "Linux Mode", fg="red", image=linPhoto)
button1.grid(row=0,column=1,pady=60)


#Develop Mode
developBtn = Button(app, text = "Develop Mode", image=devPhoto, fg="green", command = developCallBack)
developBtn.grid(row=1,column=1,pady=60)

#Play Mode
playBtn = Button(app, text = "Play Mode", fg="orange", image=playPhoto)
playBtn.grid(row=2,column=1,pady=60)


#Kick off the event loop
root.mainloop()
