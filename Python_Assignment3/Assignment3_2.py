def MaximumX(No):
    Data=[]
    iMax=0
    print("Enter the element:")
    for i in range(No):
        insertX=int(input())
        Data.append(insertX)

    for i in range(No):
        if(Data[i]>iMax):
            iMax=Data[i]

       
    return iMax  

        

        



def main():
    Ret=0
    print("Enter the size of Array:")
    value=int(input())
    Ret=MaximumX(value)
    print("maximum number  from  list elements:",Ret)

if __name__=="__main__":
    main()