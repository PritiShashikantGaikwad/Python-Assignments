class Calculate:
    def __init__(self,No1,No2):
        self.No1=No1
        self.No2=No2

    def Add(self):
        Ans=self.No1+self.No2
        return Ans
    def Subtract(self):
        ans=self.No1-self.No2
        return ans
    def Multiplication(self):
        ans=self.No1*self.No2
        return ans
    def Division(self):
        ans=self.No1/self.No2
        return ans


def main():
    print("Enter first number:")
    value=int(input())   
    print("Enter second number:")
    value2=int(input())  
    obj=Calculate(value,value2)

    Ret=obj.Add()
    print("Addition is:",Ret)

    Ret2=obj.Subtract()
    print("subtraction is:",Ret2)

    Ret3=obj.Multiplication()
    print("Multiplication is:",Ret3)

    Ret4=obj.Division()
    print("Division is:",Ret4)
    print("Enter first number:")

    value=int(input())   
    print("Enter second number:")
    value2=int(input())  
    obj2=Calculate(value,value2)
    Ret=obj2.Add()
    print("Addition is:",Ret)

    Ret2=obj2.Subtract()
    print("subtraction is:",Ret2)

    Ret3=obj2.Multiplication()
    print("Multiplication is:",Ret3)

    Ret4=obj2.Division()
    print("Division is:",Ret4)
   

if __name__=="__main__":
    main()

