#! /usr/bin/env python3.4
#chapter 13 GUI

import sys
from tkinter import *
popupper = (len(sys.argv) > 1)

def dialog():
	win = Toplevel()
	Label(win, text = 'Do You Always Do').pack()
	Button(win, text= 'Now click this one', command = win.destroy).pack()
	if popupper:
		win.focus_set()
		win.grab_set()
		win.wait_window()
	print('You better obey me...')

root = Tk()
Button(root, text='Click me', command = dialog).pack()
root.mainloop()















