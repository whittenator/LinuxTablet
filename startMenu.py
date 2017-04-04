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
helpPhoto = PhotoImage(file="helpPic.png")

#Background Image
#backgroundPhoto = PhotoImage(file="Background.png")
  
#Runs the i7 application - requires the 'Linux_all' variant of the Inform 7 installation 
def developCallBack():
	#subprocess.Popen("i7") 
	subprocess.Popen(['lxterminal',"--geometry=126x36",'--working-directory=/usr/local/bin/'])

#Runs the Gargoyle interpreter - requires the 'gargoyle-free' package installed
def playCallBack():
	subprocess.Popen("gargoyle-free")

def on_closing():
     messagebox.askokcancel("Quit", "YOU MUST PICK A MODE!")

def linuxCallBack():
        root.destroy()

def helpCallBack():
                #modify help box window
	top = Toplevel()
	top.title("Help Menu")
	top.geometry("500x440")
	top.resizable(False, False)
	#puts scrollbar into window
	scrollbar = Scrollbar(top)
	scrollbar.pack(side=RIGHT, fill=Y)
	#inserts textbox into window
	textbox = Text(top, height=4, width=50, wrap=WORD, font='roboto')
	textbox.pack(side=LEFT, fill=BOTH)
	scrollbar.config(command=textbox.yview)
	textbox.config(yscrollcommand=scrollbar.set)
	textbox.insert(END, """                                     Linux Tablet Help Menu

1. Linux Mode:
In this mode you can explore Linux OS, Raspbian

2. Develop Mode:
After clicking on Develop Mode, you will be prompted with a terminal. Simply type i7 and the Inform 7 terminal editor will launch

3. Play Mode:
After clicking on Play Mode, Gargoyle for Inform 7 will launch. Locate the folder named Inform7_Games. Double click on the game you want to play.

FAQ:

Q-How do I import new games?\nA-\n1.Open Linux mode\n2. Navigate to the folder where Inform 7 games are stored\n3. Drag files into this folder from a USB drive or downloaded files from the web

Q-Where can I find Infrom 7 games online?\nA-You can download games from Inform 7 website or search for games online in any search engine

Q-Where can I learn more about the Inform 7 programming language?\nA-Check out the documentation on Inform 7's website at: www.inform7.com/learn/

Q-What are the Inform 7 keywords to use when I am in a game?\nA-There are many different keywords in Inform 7 to use to interact with the game. In order to see which keywords your game uses, type 'help' when in a game. To see all keywords used by Inform 7, go to www.Inform7.com

Q-How do I develop Inform 7 games in something other than the terminal?\nA-As of now, the terminal editor is the only way to develop Inform 7 games in Raspbian.

Q-When in Linux Mode, how do I get the start menu to pop up again?\nA-You can either restart the tablet OR find the file named startMenu.py and execute it.

Linux Tablet Project Information:
Developers: Anthony Stewart, Dale Marcot, and Travis Whitten
Version: 3.0
Advisor: Professor Van Scoy
github: https://github.com/whittenator/LinuxTablet.git""")


#Modify root window
root.title("Linux Tablet Project")
root.geometry("1024x600")
root.config(bg="black")
root.attributes('-fullscreen',True)
root.resizable(False, False)
#background_label = Label(root, image=backgroundPhoto)
#background_label.place(x=0,y=0,relwidth=1,relheight=1)

#Command below takes away toolbar at top all together(BECAREFUL!)
#root.overrideredirect(1)

#Uncomment line below to make it to where the user can't leave
#root.protocol("WM_DELETE_WINDOW", on_closing)

app = Frame(root,width=800,height=480,bg="black")
app.pack(side=TOP)


#Linux Mode
button1 = Button(app, text = "Linux Mode",bg="black",bd=0, activebackground="black", highlightthickness = 0,image=linPhoto, command = linuxCallBack, cursor="man")
button1.grid(row=0,column=1,pady=30)
  
#Develop Mode
developBtn = Button(app, text = "Develop Mode", bg="black",bd=0, activebackground="black",highlightthickness = 0, image=devPhoto, command = developCallBack, cursor="pencil")
developBtn.grid(row=1,column=1,pady=30)
  
#Play Mode
playBtn = Button(app, text = "Play Mode", bg="black",bd=0,activebackground="black" ,highlightthickness = 0, image=playPhoto, command = playCallBack, cursor="gumby")
playBtn.grid(row=2,column=1,pady=30)

#Help Button
helpBtn = Button(root, text = "help", bg="black", bd=0,activebackground="black" ,highlightthickness = 0, image=helpPhoto, command = helpCallBack, cursor="question_arrow")
helpBtn.place(x=900,y=500)
#helpBtn.grid(row=2,column=3,padx=20)
 
 
#Kick off the event loop
root.mainloop()
