import os
import sys
def CompareContent(FileName1,FileName2):
    fobj=open(FileName1,'r')
    fobj2=open(FileName2,'r')

    data1=fobj.read()
    data2=fobj2.read()

    if(data1==data2):
        print("the content are same")
    else:
         print("the content are not  same")    
    

   
       

def main():
    
    CompareContent(sys.argv[1],sys.argv[2])

if __name__=="__main__":
    main()