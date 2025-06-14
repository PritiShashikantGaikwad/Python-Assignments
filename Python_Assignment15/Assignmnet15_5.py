import os
import sys

def CopyContent(sourceFile):
    iCnt=0
   

    fobj=open(sourceFile,"r")

    for line in fobj.read():
        if(line== "Marvellous")  :
            iCnt=iCnt+1

    print(iCnt)                

        
        


def main():
    FileName=sys.argv[1]
    
    CopyContent(FileName)
  

if __name__=="__main__":
    main()