class Numbers:

    def __init__(self,value):
        self.value=value

    def ChkPrime(self):
        iCnt=0
        for i in range(1,self.value+1):
            if(self.value%i==0):
                iCnt=iCnt+1
        if(iCnt==2):
            return True
        else:
            return False
    def ChkPerfect(self):
        No=0
        iSum=0
        #No=self.value
        for i in range(1,self.value+1):
            iSum=iSum+i

        if(iSum==self.value):
            return True
        else:
            return False
    def Factor(self):
        for i in range(1,self.value):
            if(i % 2==0):
                print(i)

    def SumFactors(self):
        iSum=0
        for i in range(self.value):
            if(i % 2==0):
              iSum=iSum+i
        return iSum

def main():
    print("Enter the number:")
    No=int(input())
    obj=Numbers(No)
  
    Ret=obj.ChkPrime()
    if(Ret==True):
        print("The number is prime")
    else:
        print("The number is not prime")

    ret2=obj.ChkPerfect()
    if(ret2==True):
        print("the number is perfect number")
    else:
        print("The number is not perfect")
    obj.Factor()
    Ret3=obj.SumFactors()
    print("Sum of factor is:",Ret3)

    print("Enter the number:")
    No2=int(input())
    obj2=Numbers(No2)
    Ret=obj2.ChkPrime()
    if(Ret==True):
        print("The number is prime")
    else:
        print("The number is not prime")

    ret2=obj2.ChkPerfect()
    if(ret2==True):
        print("the number is perfect number")
    else:
        print("The number is not perfect")
    obj2.Factor()
    Ret3=obj2.SumFactors()
    print("Sum of factor is:",Ret3)

if __name__=="__main__":
    main()    





                

