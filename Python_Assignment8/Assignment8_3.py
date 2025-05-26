import threading

def EvenList(no):
    iSum=0
    
    print("inside even function :")
    for i in no:
     
        if(i %2==0):
            iSum=iSum+i
    print("Addition of even number is:",iSum)

def OddList(no):
    
    print("inside odd function :")
    iSum=0
    
    for i in no:
        if(i %2==1):
            iSum=iSum+i
    print("Addition of odd number is:",iSum)        
        

def main():
    data=[]
    print("print inside main")
    print("Enter the size of list")
    size=int(input())

    for i in range(size):
        no=int(input())
        data.append(no)
       

   
    t1=threading.Thread(target=EvenList,args=[data])
    t2=threading.Thread(target=OddList,args=[data])
    
    t1.start()
    t2.start()
    t1.join()
    t2.join()
   

if __name__=="__main__":
    main()  