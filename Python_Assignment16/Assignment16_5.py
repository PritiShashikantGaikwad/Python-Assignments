import os
def FileDisplay(Value):
    iCnt=0
    fobj=open(Value,"r")
    Ret=os.path.exists(Value)

    if(Ret==True):
        for line in fobj.read():
            
            if(line==" "):
                iCnt=iCnt+1
                if(iCnt>=5):
                    print(line)
      
    
    else:
        print("File not exists")



    


def main():
    print("Enter the file name:")
    FileName=input()
    FileDisplay(FileName)

if __name__=="__main__":
    main()