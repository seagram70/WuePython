#!/usr/bin/env python
# -*- encoding: utf-8 -*-



import sys
import os
import Tkinter
import tkMessageBox
top=Tkinter.Tk()

def helloCallBack():
    os.system('SendEmail.py')

B=Tkinter.Button(top,text="hello",command= helloCallBack)
B.pack()
top.mainloop()