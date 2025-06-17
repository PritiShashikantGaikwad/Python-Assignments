import os
import sys
def CopyContentOfFile(sourceFile,DestinationFile):
    fobj=open(sourceFile,'r')
    fobj2=open(DestinationFile,'w')
    for line in fobj.read():
        fobj2.write(line)

    fobj.close()
    fobj2.close()    

   
       

def main():
    
    CopyContentOfFile(sys.argv[1],sys.argv[2])

if __name__=="__main__":
    main()