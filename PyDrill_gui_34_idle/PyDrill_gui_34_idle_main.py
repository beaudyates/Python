from tkinter import *
import tkinter as tk
import PyDrill_gui_34_idle_gui
import PyDrill_gui_34_idle_func


class ParentWindow(Frame):  
    def __init__(self, master):
        Frame.__init__(self, master)

        PyDrill_gui_34_idle_func.center_window(self,530,300)
        self.master.title("Python GUI end drill")
        self.master.configure(bg="#F0F0F0")
        
        self.master.protocol("WM_DELETE_WINDOW", lambda: PyDrill_gui_34_idle_func.ask_quit(self))
        
        PyDrill_gui_34_idle_gui.load_gui(self)
        
    
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
