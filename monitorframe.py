from tkinter import *
import Subprocess as sub
from tkinter import *
import tkinter as tk # Python 3
from queue import Queue, Empty # Python 3


fname = "phonenum.txt"
ph_count =0
    
def number_reader():
    with open(fname, 'r') as f:
        for line in f:
            phnum = [line for line in f.readlines()]
    return phnum
         
         

class MyLabel(LabelFrame):     #Proc_List):
    def __init__(self, master, phnum):
        LabelFrame.__init__(self, master,  text=phnum,height= 69, width=146)
        self.master = master
        self.master.grid_propagate(0)
        self.Frame = Frame(self,height= 70, width=90,bg="blue")
        self.Frame.grid(sticky='nswe')
        self.Frame.rowconfigure(0, weight=1)
        self.Frame.columnconfigure(0, weight=1)
        self.Frame.grid_propagate(0)
        self.Frame.grid(row=0,column=0)
        
        
        def startrobot():
            botstatus = sub.DisplaySubprocessOutputDemo(self.Frame,phnum,bt)
            bt.config(state='disable')
            
              
            
        bt = Button(self.Frame, text='Start', fg='white', bg='#44F',command=startrobot)
        bt.grid(sticky='nswe')
        
        bt.grid(row=0,column=0)
        
        
        
        
        
def grider(phnum,root,List):
    COLUMNS = 10
    ROWS = 4
    for i in range(COLUMNS*ROWS):
        try:
            row, col = divmod(i, COLUMNS)
            bobo = MyLabel(root, phnum[i]).grid(row=row,column=col)
            List[phnum[i]].extend((bobo,row,col))
        except IndexError:
            phnum = ''
    return  

def refresh(phnum,root,List):
    def ch():   
        for i in range(4*10):
            try:
                row, col = divmod(i, 10)
                Row=List[phnum[i]][1]
                COLU=List[phnum[i]][2]
                #print(i)
            except:
                continue
         #print (Row,COLU)
        return [Row , COLU]
    ch=ch()
    for i in range(4*7):
      try:
        if ch == [List[phnum[i]][1],List[phnum[i]][2]]:
          try:
            row , col = divmod(i+1 , 10)
            bobo = MyLabel(root, phnum[i+1]).grid(row=row,column=col)
            
            List[phnum[i+1]].extend((bobo,row,col))
            #print(List)
          except IndexError:
            phnum = ''
      except:
        break
            