import os

def FileRead(FileName):
    Names=[]
  
    Ret=os.path.exists(FileName)
    fobj=open(FileName,"r")

    if(Ret==True):
        print("The file is already exists..")
        Data=fobj.read()
        print(Data)
    else: 
     print("file is not exists:")

def main():
    print("Enter the  name of file:")
    Value=input()

    FileRead(Value)


if __name__=="__main__":
    main() 