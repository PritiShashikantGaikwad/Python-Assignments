import os
import datetime
import time
import shutil
import schedule
import sys

def Disaply(Directory_Name="Assignment17"):
    BackCount=0
    NoofFiles=0
    timestamp=datetime.datetime.now()
    

    for FolderName ,SubFolderName,FileName in os.walk(Directory_Name):
            print("Folder name is:"+FileName)
            for i in FileName:
                    FileBack="MarvellousLog%s.log" %(timestamp)
                    FileBack=FileBack.replace(" ","_")
                    FileBack=FileBack.replace(":","_")
                    obj=open(FileBack,"w")
    
                    fobj=open(i,"r")
                    data=fobj.read
                    obj.write(data)

           

                 
                 

                 


def main():
      
      schedule.every(20).seconds.do(Disaply,sys.argv[1])

      while True:
            schedule.run_pending()
            time.sleep(1)


if __name__=="__main__":
      main()

            
                  
                  