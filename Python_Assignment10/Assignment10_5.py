from functools import reduce

def chkPrime(No):
    iCnt=0
    for i in  range(1,No):
        if(No %i ==0):
            iCnt=iCnt+1
    if(iCnt<=2):
        return No         

Add=lambda No:No*2

def max(Max,No):
    
    for i in range(No):
        if(No>Max):
            Max=No
    return Max        




def main():
    data=[2,70,11,10,17,23,31,77]
    fdata=list(filter(chkPrime,data))
    print("Data from filter:",fdata)

    mData=list(map(Add,fdata))
    print("The data using map:",mData)

    rData=reduce(max,mData)
    print("The data using reduce:",rData)


if __name__=="__main__":
    main()