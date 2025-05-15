def MinimumX(No):
    Data=[]
    iMin=0
    print("Enter the element:")
    for i in range(No):
        insertX=int(input())
        Data.append(insertX)


    iMin=Data[0]
    for i in range(No):
        if(Data[i]<iMin):
            iMin=Data[i]

       
    return iMin  

        

        



def main():
    Ret=0
    print("Enter the size of Array:")
    value=int(input())
    Ret=MinimumX(value)
    print("maximum number  from  list elements:",Ret)

if __name__=="__main__":
    main()