import os

def StudentFile(FileName):
   
  
    Ret=os.path.exists(FileName)
    fobj=open(FileName,"w")

    if(Ret==True):
        print("The file is already exists..")
    else: 
     for i in range(10):
        no=int(input())
       
        fobj.write(str(no)+"\n")
    fobj.close()    
     


def main():
    print("Enter the  name of file:")
    Value=input()

    StudentFile(Value)


if __name__=="__main__":
    main()    
