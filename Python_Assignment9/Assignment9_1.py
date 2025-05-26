import threading
import time
def Display():
    for i in range(1,5+1):
        print(i)
        time.sleep(1)


def Display2():
    for i in range(1,5+1):
        print(i)
        time.sleep(1)

def Display3():
    for i in range(1,5+1):
        print(i) 
        time.sleep(1)

def main():
    t1=threading.Thread(target=Display) 
    t2=threading.Thread(target=Display2) 
    t3=threading.Thread(target=Display3) 

    t1.start()  
    t2.start()  
    t3.start() 

    t1.join()
    t2.join()
    t3.join()


if __name__=="__main__":
    main()    

