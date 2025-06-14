import os
import sys
import filecmp

def CopyContent(sourceFile,DestFile):        #this first ways to comapre to files contents
    fobj=open(sourceFile,"r")
    fobj2=open(DestFile,"r")
    data1=fobj.read()
    data2=fobj2.read()

    if(data1==data2):
        print("both file contents are same:")

    else:
         print("both file  contents are not  same:")

"""def CopyContent(sourceFile,DestFile):           #second way to comapre the files contents
     
     Ret=filecmp.cmp(sourceFile,DestFile)
     if(Ret==True):
          print("both file contents are same:")

     else:
         print("both file  contents are not  same:")"""
         
def main():
    FileName=sys.argv[1]
    FileName2=sys.argv[2]
    CopyContent(FileName,FileName2)

if __name__=="__main__":
    main()