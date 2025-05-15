
def ChkPrime(No):
    iCnt=0
    Data=[]
    for i in range (list(No)):
        if(No %i ==0):
            iCnt=iCnt+1

        if(iCnt==2):
            iSum=iSum+Data[i]

    return iSum        
                

       