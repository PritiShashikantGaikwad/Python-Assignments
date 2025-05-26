import threading

def Display1(no):
    print("inside 1 st function")
    for i in range(1,no+1,1):
        print(i)
def Display2(no):
    
    print("inside 2 st function")
    for i in range(no,0,-1):
        print(i)

def main():

    t1=threading.Thread(target=Display1,args=(50,))
    t2=threading.Thread(target=Display2,args=(50,))   

    t1.start()
    t1.join()

    t2.start()
    t2.join()     

if __name__=="__main__":
    main()