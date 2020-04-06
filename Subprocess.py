#!/usr/bin/python
"""
- read output from a subprocess in a background thread
- show the output in the GUI
"""
import sys
from itertools import islice
from subprocess import Popen, PIPE
from textwrap import dedent
from threading import Thread
import signal
import os

try:
    import Tkinter as tk
    from Queue import Queue, Empty
except ImportError:
    import tkinter as tk # Python 3
    from tkinter import *
    from queue import Queue, Empty # Python 3

def iter_except(function, exception):
    """Works like builtin 2-argument `iter()`, but stops on `exception`."""
    try:
        while True:
            yield function()
    except exception:
        return

class DisplaySubprocessOutputDemo:
    def __init__(self, root, number,btn):
        self.root = root

        # start dummy subprocess to generate some output
        self.process = Popen([sys.executable,'btc.py', number], stdout=PIPE, stdin=PIPE, stderr=PIPE,shell=True)
        
        
        #self.process.stdin.write(b'\n')
        
        # launch thread to read the subprocess output
        #   (put the subprocess output into the queue in a background thread,
        #    get output from the queue in the GUI thread.
        #    Output chain: process.readline -> queue -> label)
        q = Queue(maxsize=1024)  # limit output buffering (may stall subprocess)
        t = Thread(target=self.reader_thread, args=[q])
        t.daemon = True # close pipe if GUI process exits
        t.start()
        # show subprocess' stdout in GUI
        def quitt():
             print(self.process.pid)
             print(os.getpid())
             response = self.process.communicate()[0]
             print(response)
             #os.kill(os.getpid(), signal.SIGTERM)
             #os.kill(self.process.pid, signal.SIGTERM)
        
        self.label = tk.Label(root, text="  ", font=(None, 9), width=10)
        self.label.grid(sticky='nswe')               # pack(ipadx=4, padx=4, ipady=4, pady=4)
        self.button = tk.Button(root, text="close", command=quitt)
        self.button.grid()               # pack(ipadx=4, padx=4, ipady=4, pady=4)        
        self.update(q) # start update loop
        #print(self.process.pid)

    def reader_thread(self, q):
        """Read subprocess output and put it into the queue."""
        try:
            with self.process.stdout as pipe:
                for line in iter(pipe.readline, b''):
                    
                    q.put(line)
        finally:
            q.put(None)

    def update(self, q):
        """Update GUI with items from the queue."""
        for line in iter_except(q.get_nowait, Empty): # display all content
            if line is None:
                self.quit()
                return
            else:
                self.label['text'] = line
                if line == b'working  \r\n': 
                    self.label.configure(foreground="white", bg ="green" )
                elif line == b'Sleeping \r\n':
                    self.label.configure(foreground="green", bg ="yellow" )                # update GUI
                break # display no more than one line per 1000 milliseconds
        self.root.after(3000, self.update, q) # schedule next update

    def quit():
        self.process.kill() # exit subprocess if GUI is closed (zombie!)
        self.root.destroy()

"""
root = tk.Tk()
app = DisplaySubprocessOutputDemo(root,'+21692125206')
app1= DisplaySubprocessOutputDemo(root,'+21697601208')
root.protocol("WM_DELETE_WINDOW", app.quit)
# center window
root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))
root.mainloop()"""