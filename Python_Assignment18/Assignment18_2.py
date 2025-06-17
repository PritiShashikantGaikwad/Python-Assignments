import os
def ReadFile(FileName):
    Ret=os.path.exists(FileName)

    if(Ret==False):
         print("The file is not exists:"+FileName)
    else:
        fobj=open(FileName,'r')
        data=fobj.read()
        fobj.close()
        print("The content from the file:"+data)
       

def main():
    print("Enter the filename")
    FileName=input()
    ReadFile(FileName)

if __name__=="__main__":
    main()