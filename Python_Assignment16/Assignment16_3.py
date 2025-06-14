import os

def FileRead(FileName):
    chars=0
    lines=0
    words=0
  
    Ret=os.path.exists(FileName)
    fobj=open(FileName,"r")

    if(Ret==True):
        print("The file is already exists..")
        for line in fobj.read():
           if(line==" "):
              words=words+1
            
           if(line=="\n"):
              lines=lines+1
        print("Number of lines :",lines)
        print("Number of words s are:",words) 
        print("number of chracters are:",lines*words)    

         



    else: 
     print("file is not exists:")

def main():
    print("Enter the  name of file:")
    Value=input()

    FileRead(Value)


if __name__=="__main__":
    main() 