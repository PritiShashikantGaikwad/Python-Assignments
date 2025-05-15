from functools import reduce
def ChkNumber(No):
   
        return  ((No>=70) and (No<=90))
def Add(No):
        return No+10

def Sum(No1,No2):
        return No1*No2

def main():
        
        Data=[]
        print("Enter the number of elements :")
        size=int(input())

        for i in range(size):
                no=int(input())
                Data.append(no)

        FData=list(filter(ChkNumber,Data))
        print("the Data from the list using filter",FData)
        MData=list(map(Add,FData))
        print("the Data after Adding 10 inside  list using map",MData)

        RData=reduce(Sum,MData)
        print("the final product form the reduce:",RData)


if __name__=="__main__":
        main()        
    
