import subprocess as sub
from tkinter import *
import tkinter as tk # Python 3
from queue import Queue, Empty # Python 3
from telethon.errors import FloodWaitError
import telethon
from tkinter import messagebox
import monitorframe as gr

def Connection(phone_number,root,monitorframe,Proc_List):
 process = sub.Popen(['python','teleconnect.py', phone_number], stdout=sub.PIPE, stdin=sub.PIPE, stderr=sub.PIPE,shell=True)

 stdout, stderr = process.communicate()
 
 
      
 if stdout== b'Please enter the code you received: ':
   # 
   val = StringVar()
   print('input catched')
   inputv = Entry(root,textvariable=val)
   inputv.grid(row=0 , column=10)
   
   def vasy():
    recon = sub.Popen(['python','teleconnect.py', phone_number], stdout=sub.PIPE, stdin=sub.PIPE, stderr=sub.PIPE,shell=True)
    recon.stdin.write(val.get().encode('utf-8'))
    print(recon.communicate()[0])
    recon.stdin.close()
    messagebox.showinfo("Information","connect successful")
    gr.refresh(gr.number_reader(), monitorframe, Proc_List)
    inputv.destroy()
    submit.destroy()
   submit = Button(root,text="ok",command=vasy)
   submit.grid(row=1,column=10)
   
    
 else:
   messagebox.showwarning("Warning",stdout.decode(encoding="utf-8"))
   print(stderr.decode(encoding="utf-8"))
   with open(fname) as f:
        datafile = f.readlines()
        for line in datafile:
            if addinput.get() in line:
                line = ''