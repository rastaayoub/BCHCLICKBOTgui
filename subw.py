import subprocess as sub
import sys

def balance(phnum,List):

    process = sub.Popen([sys.executable,'withdraw.py', phnum], stdout=sub.PIPE, stdin=sub.PIPE, stderr=sub.PIPE,shell=True)
    stdout , stderr = process.communicate(b'0')
    List[phnum].extend((stdout.decode(encoding="utf-8")[2:],stdout.decode(encoding="utf-8")[0:1]))
    print(List[phnum][3])
    
    
def withdraw(phnum,adress,List):
    cmd =[sys.executable,'wth.py', adress,phnum]
    print(cmd)
    process = sub.Popen(cmd, stdout=sub.PIPE, stdin=sub.PIPE, stderr=sub.PIPE,shell=True)
    stdout , stderr = process.communicate(b'0')
    print(stdout)
