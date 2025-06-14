import os

def main():
   print("Enter the file name")
   FileName=input()

   ret=os.path.exists(FileName)
   if(ret==True):
       print("The file is exits")
       fobj=open(FileName,"r")
       data=fobj.read()
       print(data)
   else :
       print("The file is not exits")  
       
if __name__=="__main__":
    main()
