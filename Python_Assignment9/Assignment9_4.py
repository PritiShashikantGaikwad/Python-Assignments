import threading
import multiprocessing
import time
"""def Display(no):
    iSum=0
    for i in range(1,no):
        iSum=iSum+i
    return iSum"""
    

def Display2(no):
    iSum=0
    for i in range(1,no):
        iSum=iSum+i
    print(iSum)

def Display3(no):
    iSum=0
    for i in range(1,no):
        iSum=iSum+i
    print(iSum)

def main():
    """start_time=time.time()
    ret=Display(10000000000)
    print(ret)
    end_time=time.time()
    print("Time required for normal function is:",end_time-start_time)
    """
    start_time=time.time()
    t1=threading.Thread(target=Display2,args=[10000000000])
    t1.start()
    t1.join()
    end_time=time.time()
    print("Time required for multithreading  is:",end_time-start_time)

    start_time=time.time()
    p1=multiprocessing.Process(target=Display3,args=[10000000000])
    p1.start()
    p1.join()
    end_time=time.time()
    print("Time required for Multiprocessing  is:",end_time-start_time)

if __name__=="__main__":
    main()


    