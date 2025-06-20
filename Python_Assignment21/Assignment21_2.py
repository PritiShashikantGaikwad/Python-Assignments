import psutil
import os
import time
import sys

def CreateLog(FolderName,Data):
    if not os.path.exists(FolderName):
        os.mkdir(FolderName)
    
    timestamp=time.ctime()
    timestamp=timestamp.replace(":","_")
    timestamp=timestamp.replace(" ","_")
    timestamp=timestamp.replace("/",":")

    FileName=os.path.join(FolderName,"Marvellous%s.log"%(timestamp))
    Border="*"*80
    fobj=open(FileName,"w")
    fobj.write(Border+"\n")
    fobj.write("This is automation Script ")
    fobj.write("This file is created at:"+str(time.ctime())+"\n")
    fobj.write(Border+"\n")
    for value in Data:
            fobj.write(str (value)+"\n")
            
    fobj.write(Border+"\n")
    fobj.close()

def ProcessDetails(processname):

    listprocess=[]

    for proc in psutil.process_iter(['name','pid']):
        if proc.info['name']==processname:
              listprocess.append(proc)
            
            
    
    return listprocess
def main():

    
           Arr=ProcessDetails("Code.exe")
           CreateLog("MarvellousLogProcess",Arr)

          
   
     

if __name__=="__main__":
    main()