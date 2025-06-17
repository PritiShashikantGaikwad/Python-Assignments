import os
import sys
def CountString(FileName1):
    iCount=0
    stringcmp="Marvellous"
    fobj=open(FileName1,'r')

    for i in fobj.read():
        words=slice(i)
        if(words==stringcmp):
            iCount=iCount+1

    return iCount        
    

   
       

def main():
    
    REt=CountString(sys.argv[1])
    print(REt)

if __name__=="__main__":
    main()