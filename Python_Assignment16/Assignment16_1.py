import os

def StudentFile(FileName):
    Names=[]
  
    Ret=os.path.exists(FileName)
    fobj=open(FileName,"w")

    if(Ret==True):
        print("The file is already exists..")
    else: 
     for i in range(5):
        Names=input()
        fobj.write(Names+"\n")


def main():
    print("Enter the  name of file:")
    Value=input()

    StudentFile(Value)


if __name__=="__main__":
    main()    

