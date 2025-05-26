import threading

def Even(no):
    print("inside even function :")
    for i in range(1,no+1):
        if(i%2==0):
            print(i)

def Odd(no):
    
    print("inside odd function :")
    for i in range(1,no+1):
        if(i %2 !=0):
            print(i)

def main():
    print("print inside main")
   
    t1=threading.Thread(target=Even,args=(20,))
    t2=threading.Thread(target=Odd,args=(20,))
    
    t1.start()
    t1.join()
    t2.start()
    t2.join()
    print("End of main")

if __name__=="__main__":
    main()    