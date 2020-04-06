from tkinter import *
import Subprocess as sub
from tkinter import *
import tkinter as tk # Python 3
from queue import Queue, Empty # Python 3
import monitorframe as gr
from monitorframe import MyLabel
import az
from tkinter import messagebox
#vars:
up=10
down=1
balance=0.00235

#functions:
fname = "phonenum.txt"
Proc_List={}
def refresh():
    gr.refresh(gr.number_reader(), monitorframe, Proc_List)
    print('-------------------------------------------------------')
    print(Proc_List)
    
    
def Dashboard_window():

    DashboardWin = Toplevel(root)
    DashboardWin.title('Dashboard')
    DashboardWin.geometry('1045x540')
    DashboardWin.resizable(width=False, height=False)
    dashboard.config(state='disable')

    def quit_win():
        DashboardWin.destroy()
        dashboard.config(state='normal')
       
        
    def Withdraw_window():

        WithdrawWin = Toplevel(DashboardWin)
        WithdrawWin.title('Withdraw')
        WithdrawWin.geometry('300x200')
        WithdrawWin.resizable(width=False, height=False)
        withdrawbtn.config(state='disable')

        def quit_WithdrawWin():
           WithdrawWin.destroy()
           withdrawbtn.config(state='normal')
        
        withdrawquit = Button(WithdrawWin, text='quit', bg="yellow", command=quit_WithdrawWin)
        withdrawquit.pack(side=BOTTOM, padx=5)
     
   #userbot monitor    
   # monitorframe=LabelFrame(DashboardWin, text="Userbots Monitor", height= 350, width=400)
   # monitorframe.pack(fill=X)
  
   #robot frames:
    #userbot count function:
    
    fname = "phonenum.txt"
    ph_count =0
    
    #number counting
    with open(fname, 'r') as f:
       for line in f:
         ph_count += 1
         
         
    #phone numbers to array
    with open(fname, 'r') as f:
       for line in f:
         phnum = [line for line in f.readlines()]
         
         
    print(ph_count, phnum)
    num=0
    bot={}
    bbut={}
    class MyLabel(LabelFrame):
       def __init__(self, master, phnum):
        LabelFrame.__init__(self, master,  text=phnum)
        Frame(self,height= 20, width=100).pack()
        def startrobot():
            botstatus = sub.DisplaySubprocessOutputDemo(self,phnum)
            print(botstatus['text'])
            
            
        Button(self, text='Rest', fg='white', bg='#44F',command=startrobot).pack(side=LEFT)
        Button(self, text='Close', fg='white', bg='#44F',command=self.destroy).pack(side=RIGHT)
        
        def startrobot():
            sub.DisplaySubprocessOutputDemo(self,phnum)
    COLUMNS = 10
    ROWS = 4
    for i in range(COLUMNS*ROWS):
       try:
        row, col = divmod(i, COLUMNS)
        print(phnum[i])
        MyLabel(monitorframe, phnum[i]).grid(row=row,column=col)
       except IndexError:
        phnum = ''

   # for r in range(4):
    #  for c in range(6):
     #    num+=1
      #   bot[num] =LabelFrame(monitorframe, text=num,
       #  borderwidth=1 ,  height= 86, width=132).grid(row=r,column=c)
         
    
   #button frame
    btnframe=LabelFrame(DashboardWin, text="operations", height= 100, width=400)
    btnframe.pack(fill=X, side=BOTTOM)
    
   #balance frame
    totalbalance=LabelFrame(btnframe, text="TOTAL BALANCE", height= 100, width=100)
    totalbalance.pack(fill=X, side=LEFT, padx=3)
    textt=Label(totalbalance, text=balance)
    textt.pack()
    
   #withdraw button 
    withdrawbtn = Button(btnframe, text='Withdraw', bg="yellow", command=Withdraw_window)
    withdrawbtn.pack(side=LEFT, padx=5)
    
   #Start all/ Stop all/ Quit btns:
    QuitDashboard = Button(btnframe, text='Return', command=quit_win)
    QuitDashboard.pack(side=RIGHT, padx=5)
    
    StopAll = Button(btnframe, text='Stop All', bg="Red",fg="white", command=quit_win)
    StopAll.pack(side=RIGHT, padx=5)
    
    StartAll = Button(btnframe, text='Start All', bg="green", fg="white", command=quit_win)
    StartAll.pack(side=RIGHT, padx=5)
    
    DashboardWin.protocol("WM_DELETE_WINDOW", quit_win) 
    
def Settings_window():

    SettingsWin = Toplevel(root)
    SettingsWin.title('Settings')
    SettingsWin.geometry('300x400')
    SettingsWin.resizable(width=False, height=False)
    settings.config(state='disable')

    def quit_win():
        SettingsWin.destroy()
        settings.config(state='normal')

    QuitSettings = Button(SettingsWin, text='Return', command=quit_win)
    QuitSettings.pack(side=BOTTOM)

    SettingsWin.protocol("WM_DELETE_WINDOW", quit_win)
    
def Accounts_window():

    AccountsWin = Toplevel(root)
    AccountsWin.title('Dashboard')
    AccountsWin.geometry('200x300')
    AccountsWin.resizable(width=False, height=False)
    accounts.config(state='disable')

    def quit_win():
        AccountsWin.destroy()
        accounts.config(state='normal')

    QuitAccounts = Button(AccountsWin, text='Return', command=quit_win)
    QuitAccounts.pack(side=BOTTOM)

    AccountsWin.protocol("WM_DELETE_WINDOW", quit_win)

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
    #print(Proc_List) 
    #print(Proc_List[gr.number_reader()[0]])    
    #sc = gr.grider(gr.number_reader(), monitorframe, Proc_List)
gr.grider(gr.number_reader(), monitorframe, Proc_List)
print(Proc_List)

    
    
    
   

#buttons widget

btnwd= LabelFrame(root, text="options", height= 170, width=240)
btnwd.grid(row=1, column=0)

dashboard=Button(btnwd, text="Refresh", command=refresh)
dashboard.pack(side=TOP)

settings=Button(btnwd, text="Settings", command=Settings_window)
settings.pack(side=LEFT)

accounts=Button(btnwd, text="Accounts", command=Accounts_window)
accounts.pack(side=RIGHT)



#Processus widget

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



    
#moniframe()


root.mainloop()