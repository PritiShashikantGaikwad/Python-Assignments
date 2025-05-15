from functools import reduce

    


def main():
        
        Data=[]
        print("Enter the number of elements :")
        size=int(input())

        for i in range(size):
                no=int(input())
                Data.append(no)

        FData=list(filter((lambda No: No % 2==0),Data))
        print("the Data from the list using filter",FData)
        MData=list(map(lambda No:No**2,FData))
        print("the Data after Adding 10 inside  list using map",MData)

        RData=reduce(lambda No1,No2:No1+No2,MData)
        print("the final product form the reduce:",RData)


if __name__=="__main__":
        main()        
    