def ArrayX(No):
    Data=[]
    iSum=0
    print("Enter the element:")
    for i in range(No):
        insertX=int(input())
        Data.append(insertX)

    for i in range(No):

        iSum=iSum+Data[i]
    return iSum    

        

        



def main():
    Ret=0
    print("Enter the size of Array:")
    value=int(input())
    Ret=ArrayX(value)
    print("Addition of list elements:",Ret)

if __name__=="__main__":
    main()
