from tkinter import *
import tkinter as tk
import PyDrill_gui_34_idle_main
import PyDrill_gui_34_idle_func


def load_gui(self):
        
	#buttons   
	self.dailyButton = tk.Button(self.master,width=18,height=1, text = 'Daily Folder', command = lambda: PyDrill_gui_34_idle_func.getDailyPath(self))
	self.dailyButton.grid(row=1,column=0,padx=(25,0),pady=(45,10),sticky=W)
	self.destButton = tk.Button(self.master, width=18, height=1, text = 'Destination Folder', command = lambda: PyDrill_gui_34_idle_func.getDestPath(self))
	self.destButton.grid(row=4,column=0,padx=(25,0),pady=(45,10),sticky=W)
	self.checkButton = tk.Button(self.master, width=18, height=1, text = 'File Check', command = lambda: PyDrill_gui_34_idle_func.copyFiles(self))
	self.checkButton.grid(row=8,column=0,padx=(25,0),pady=(45,10),sticky=W)
		
	#entry wigits for source path and destination path
	self.dail = StringVar()
	self.dailyPathLabel = tk.Entry(width=50, textvariable = self.dail)
	self.dailyPathLabel.grid(row=1,column=2, padx=(25,0),pady=(45,10))
	self.dest = StringVar()
	self.destPathLabel = tk.Entry(width=50, textvariable = self.dest)
	self.destPathLabel.grid(row=4,column=2, padx=(25,0),pady=(45,10))
	
    
