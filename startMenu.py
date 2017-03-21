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
devPhoto = PhotoImage(file="DevelopMode.png")
linPhoto = PhotoImage(file="LinuxMode.png")
playPhoto = PhotoImage(file="PlayMode.png")

#Background Image
backgroundPhoto = PhotoImage(file="Background.png")
  
#Runs the i7 application - requires the 'Linux_all' variant of the Inform 7 installation 
def developCallBack():
	#subprocess.Popen("i7") 
	subprocess.Popen(['lxterminal',"--geometry=212x127",'--working-directory=/usr/local/bin'])
	
	#instructions box
 	top = Toplevel()
	top.title("Instructions")
	msg = Message(top, text="Welcome to Develop Mode!\nTo begin developing Inform 7 games\ntype "bin/i7" into the terminal that just popped up!\n")
	msg.pack()
	btn = Button(top, text="Dismiss", command=top.destroy)
	btn.pack()
	
#Runs the Gargoyle interpreter - requires the 'gargoyle-free' package installed
def playCallBack():
	subprocess.Popen("gargoyle-free")

def on_closing():
     messagebox.askokcancel("Quit", "YOU MUST PICK A MODE!")

def linuxCallBack():
	sys.exit()
	 
#Modify root window
root.title("Linux Tablet Project")
root.geometry("800x480")
root.resizable(False, False)
background_label = Label(root, image=backgroundPhoto)
background_label.place(x=0,y=0,relwidth=1,relheight=1)

#Command below takes away toolbar at top all together(BECAREFUL!)
#root.overrideredirect(1)

#Uncomment line below to make it to where the user can't leave
#root.protocol("WM_DELETE_WINDOW", on_closing)

app = Frame(root,width=800,height=480,bg="black")
#The line below gets rid of menus and all
#root.overrideredirect(1)
app.pack(side=TOP)


#Linux Mode
button1 = Button(app, text = "Linux Mode",bg="black",bd=0, highlightthickness = 0,image=linPhoto, command = linuxCallBack, cursor="man")
button1.grid(row=0,column=1,pady=30)
  
#Develop Mode
developBtn = Button(app, text = "Develop Mode", bg="black",bd=0, highlightthickness = 0, image=devPhoto, command = developCallBack, cursor="pencil")
developBtn.grid(row=1,column=1,pady=30)
  
#Play Mode
playBtn = Button(app, text = "Play Mode", bg="black",bd=0, highlightthickness = 0, image=playPhoto, command = playCallBack, cursor="gumby")
playBtn.grid(row=2,column=1,pady=30)
 
 
#Kick off the event loop
root.mainloop()
