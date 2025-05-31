iCnt=0

def Display(No):
    global iCnt
    if(No !=0):
        iDigit=No%10
        if(iDigit==0):
            iCnt=iCnt+1
        No=No//10
        Display(No)
    return iCnt    

def main():
    Ret=Display(1020300)
    print(Ret)

if __name__=="__main__":
    main()                