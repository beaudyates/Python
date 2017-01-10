from tkinter import * 
import tkinter as tk
import os
import shutil
import time as t
import PyDrill_db_34_idle_main
import PyDrill_db_34_idle_gui


def center_window(self, w, h): # pass in the tkinter frame (master) reference and the w and h
    # get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

	
def getDailyPath(self):
	dailyPath = filedialog.askdirectory(initialdir = "C:\\", title = "Select your Daily Folder")	
	self.dail.set(dailyPath)
				
def getDestPath(self):
	destPath = filedialog.askdirectory(initialdir = "C:\\", title = "Select your Destination Folder") 
	self.dest.set(destPath)


def copyFiles(self):
	dail = self.dail.get()
	dest = self.dest.get()
	for f in os.listdir(dail):
		src = os.path.join(dail, f)
		dst = dest
		if checkIfMod(src):
			shutil.copy2(src, dst)
			print (os.path.join(dst,f))

        
def checkIfMod(fname):
    past24 = t.time() - 24*60*60 
    if os.path.getmtime(fname) >= past24:
        return True
    
    return False
	

def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        self.master.destroy()
        os._exit(0)



