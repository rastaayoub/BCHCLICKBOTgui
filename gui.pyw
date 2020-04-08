from tkinter import *
import Subprocess as sub
from tkinter import *
import tkinter as tk # Python 3
from queue import Queue, Empty # Python 3
import monitorframe as gr
from monitorframe import MyLabel
import az
from tkinter import messagebox
import subw as bw

#vars:
up=10
down=1
balance=0
#functions:
fname = "phonenum.txt"
Proc_List={}

def refresh():
    gr.refresh(gr.number_reader(), monitorframe, Proc_List)
        
def Settings_window():
    messagebox.showwarning("Warning","All Bots needs to be Stoped!!")
    SettingsWin = Toplevel(root)
    SettingsWin.title('Settings')
    SettingsWin.geometry('300x200')
    SettingsWin.resizable(width=False, height=False)
    withdraw.config(state='disable')
    
    def checkbalance():
        newbal = 0
        wbal = 0
        #print(len(gr.number_reader()))
        for i in range(len(gr.number_reader())):
            bw.balance(gr.number_reader()[i],Proc_List)
        print(Proc_List)    
        for i in range(len(gr.number_reader())):
            newbal +=float(Proc_List[gr.number_reader()[i]][3])
            if (float(Proc_List[gr.number_reader()[i]][3]) >0.0001):
                wbal+=float(Proc_List[gr.number_reader()[i]][3])
                #print(str(format(wbal, '.8f')))
                
        tt.configure(text=str(format(newbal, '.8f')),background='green')
        wb.configure(text=str(format(wbal, '.8f')),background='yellow')
        balancemonitor.configure(height=120)
        Label(balancemonitor, text= 'Enter your bitcash adress:').grid(row=1,columnspan=3)
        adress = Entry(balancemonitor)
        adress.grid(row=2,columnspan=3)
        
        def wth():
          messagebox.showwarning("Warning","Are you Sure?")
          for i in range(len(gr.number_reader())):
            if (float(Proc_List[gr.number_reader()[i]][3]) >0.0001):
                bw.withdraw(gr.number_reader()[i],adress.get(),Proc_List)
                Proc_List[gr.number_reader()[i]][3]='0.0'
                print(Proc_List[gr.number_reader()[i]][3])
          messagebox.showinfo("Information","Withdraw successful")
            
        
        Button (balancemonitor, text='Withdraw',command=wth).grid(row=2,column=3)
    
    def quit_win():
        SettingsWin.destroy()
        withdraw.config(state='normal')
        
    balancemonitor=LabelFrame(SettingsWin,text='Your Balance',width=230,height=60)
    balancemonitor.pack(side=TOP)
    balancemonitor.grid_propagate(0)
    
    total=LabelFrame(balancemonitor,text='Total Balance',width=100,height=50)
    total.grid(sticky='nswe')
    total.grid(row=0,column=0)
    
    tt=Label(total,text='0.000000')
    tt.pack()
    
    withdrawbal=LabelFrame(balancemonitor,text='Withdrawbal',width=100,height=50)
    withdrawbal.grid(sticky='nswe')
    withdrawbal.grid(row=0,column=2)
    wb=Label(withdrawbal,text='0.0000000')
    wb.pack()
    
    check=Button(balancemonitor, text='check',command=checkbalance)
    check.grid(row=0,column=3)

    QuitSettings = Button(SettingsWin, text='Return', command=quit_win)
    QuitSettings.pack(side=BOTTOM)

    SettingsWin.protocol("WM_DELETE_WINDOW", quit_win)
    
    
def create_in_file():
  def check():
    with open(fname) as f:
        datafile = f.readlines()
        for line in datafile:
            if addinput.get() in line:
               return True 
        return False
  if check():
      messagebox.showwarning("Warning","Phone Number is already entred")
      print(check()[1][1])
      addinput.delete(0, 'end')
  else:
        f= open("phonenum.txt","a")
        f.write("%s\n" % (addinput.get()))
        f.close()
        az.Connection("%s" % (addinput.get()),root,monitorframe,Proc_List)
        addinput.delete(0, 'end')
        
#root window params
root = Tk()
root.title("BCHCLICKBOT by AYOUB")
root.geometry("1024x600")
root.resizable(width=False, height=False)

#add new number widget

add= LabelFrame(root, text="Add new worker:", height= 70, width=400)
add.grid(row=0, columnspan=3)
addtxt=Label(add, text="Enter your phone N°:")
addtxt.grid(row=0,column=0)
addinput=Entry(add)
addinput.grid(row=0,column=1,columnspan=4)
addbtn=Button(add, text="add and run", command=create_in_file)
addbtn.grid(row=0,column=7)

#userbot monitor 

#monitorframe=LabelFrame(root, text="Userbots Monitor", height= 480, width=1024) 
 
monitorframe=LabelFrame(root, text="Userbots Monitor", height= 480, width=1024) 
monitorframe.grid_propagate(0)    
monitorframe.grid(row=2 ,rowspan=30 ,columnspan=30)
for i in range(len(gr.number_reader())):
    Proc_List[gr.number_reader()[i]] = []
gr.grider(gr.number_reader(), monitorframe, Proc_List)
print(Proc_List)

    
    
    
   

#buttons widget

btnwd= LabelFrame(root, text="options", height= 170, width=240)
btnwd.grid(row=1, column=0)

refresh=Button(btnwd, text="Refresh", command=refresh)
refresh.pack(side=LEFT,padx=5,pady=5)

withdraw=Button(btnwd, text="Withdraw", command=Settings_window)
withdraw.pack(side=RIGHT,padx=5,pady=5)



#Processus widget
"""
prswd= LabelFrame(root, text="Userbots Status:", height= 170, width=240)
prswd.grid(row=1, column=2 , sticky= E+W)

prswdup= LabelFrame(prswd, text="Bot Up:   ", height=40, width=40)
prswdup.pack(side=LEFT, fill=NONE, expand="yes")
txtup=Label(prswdup, text=up,fg="green", bg="white")
txtup.pack()

prswdown= LabelFrame(prswd, text="Bot down:", height=40, width=40)
prswdown.pack(side=RIGHT, fill=NONE, expand="yes")
txtdown=Label(prswdown, text=down, fg="red", bg="white")
txtdown.pack()
"""




root.mainloop()