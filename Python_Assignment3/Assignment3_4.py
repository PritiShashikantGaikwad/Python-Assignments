def Frequency(No,freq):
    Data=[]
    iCnt=0
    
    print("Enter the element:")
    for i in range(No):
        insertX=int(input())
        Data.append(insertX)


    iMin=Data[0]
    for i in range(No):
        if(Data[i]==freq):
            iCnt=iCnt+1

    return iCnt 

       
  

def main():
    Ret=0
    print("Enter the size of Array:")
    value=int(input())
    print("Enter the search element :")
    value2=int(input())
    Ret=Frequency(value,value2)
    print("the frequemncy of no is:",Ret)
    
    
if __name__=="__main__":
    main()