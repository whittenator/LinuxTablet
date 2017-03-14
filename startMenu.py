#!/usr/bin/python3
#simple GUI
  
import tkinter
import subprocess
import os
import time
from tkinter import *
from tkinter import messagebox

  
#Create the window
root = tkinter.Tk()

#Button Images
devPhoto = PhotoImage(file="devPic.png")
linPhoto = PhotoImage(file="linPic.png")
playPhoto = PhotoImage(file="playPic.png")
  
#Runs the i7 application - requires the 'Linux_all' variant of the Inform 7 installation 
def developCallBack():
	#subprocess.Popen("i7") 
	subprocess.Popen(['lxterminal','--working-directory=/usr/local/bin'])
 
#Runs the Gargoyle interpreter - requires the 'gargoyle-free' package installed
def playCallBack():
	subprocess.Popen("gargoyle-free")

def on_closing():
     messagebox.askokcancel("Quit", "YOU MUST PICK A MODE!")
	 
#Modify root window
root.title("Linux Tablet Project")
root.geometry("800x480")
root.resizable(False, False)
#Command below takes away toolbar at top all together(BECAREFUL!)
#root.overrideredirect(1)

#Uncomment line below to make it to where the user can't leave
#root.protocol("WM_DELETE_WINDOW", on_closing)

app = Frame(root,width=800,height=480)
app.pack(side=TOP)
  

#Linux Mode
button1 = Button(app, text = "Linux Mode", fg="red", image=linPhoto, cursor="man")
button1.grid(row=0,column=1,pady=60)
  
#Develop Mode
developBtn = Button(app, text = "Develop Mode", fg="green", image=devPhoto, command = developCallBack, cursor="pencil")
developBtn.grid(row=1,column=1,pady=60)
  
#Play Mode
playBtn = Button(app, text = "Play Mode", fg="orange", image=playPhoto, command = playCallBack, cursor="gumby")
playBtn.grid(row=2,column=1,pady=60)
 
 
#Kick off the event loop
root.mainloop()
