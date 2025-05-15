from functools import reduce
def ChkPrime(No):
   iCnt=0
   for i in range(1,No):
          if(No %i ==0):
                 iCnt=iCnt+1
          if(iCnt==2):
                return No     
                 
                 
        
def Add(No):
        return No*2

def Sum(No1,No2):
        
        if(No2>No1):
                No1=No2
        return No1        

def main():
        
        Data=[]
        print("Enter the number of elements :")
        size=int(input())

        for i in range(size):
                no=int(input())
                Data.append(no)

        FData=list(filter(ChkPrime,Data))
        print("the Data from the list using filter",FData)
        MData=list(map(Add,FData))
        print("the Data after Adding 10 inside  list using map",MData)

        RData=reduce(Sum,MData)
        print("the final product form the reduce:",RData)


if __name__=="__main__":
        main()        
    