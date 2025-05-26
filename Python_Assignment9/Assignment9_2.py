import multiprocessing

def Display(no):
    for i in no:
        print(i**2)
       




def main():
    data=[]
    print("Enter the size")
    size=int(input())
    print("Enter list elements:")
    for i in range(size):
        no=int(input())
        data.append(no)
    p1=multiprocessing.Process(target=Display,args=[data]) 
    p1.start()  
    p1.join()
  

if __name__=="__main__":
    main()    
