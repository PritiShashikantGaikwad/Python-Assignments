import multiprocessing
import os

def Display(no):
    iSum=0
    for i in range(1,no):
        if(no%i==0):
            iSum=iSum+i
    return iSum      

       
def main():
    data=[]
    result=[]
    print("Enter the size")
    size=int(input())
    print("Enter list elements:")
    for i in range(size):
        no=int(input())
        data.append(no)
    p=multiprocessing.Pool()

    result=p.map(Display,data)

    p.close()
    p.join()
    print(result)

if __name__=="__main__":
    main()