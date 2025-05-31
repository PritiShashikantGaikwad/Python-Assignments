class Arithmatic:
    def __init__(self):
         self.Value1=0
         self.Value2=0

    def Accept(self):
         print("Enter the first Value:")
         self.Value1=int(input()) 
         print("Enter the second Value:")
         self.Value2=int(input()) 

    def Addition(self):
         Ans=0
         Ans=self.Value1+self.Value2
         return Ans

    def Subtraction(self):
         Ans=0
         Ans=self.Value1-self.Value2
         return Ans
    def Multiplication(self):
         Ans=0
         Ans=self.Value1*self.Value2
         return Ans
    def Division(self):
         Ans=0
         if(self.Value2==0):
              print("ivalid number zero is not allowed")
              return -1
         Ans=self.Value1/self.Value2
         return Ans
    
def main():
     obj=Arithmatic()
     obj2=Arithmatic()

     obj.Accept()
     obj2.Accept()

     Ret=obj.Addition()
     Ret2=obj2.Addition()
     print("The Addition of obj is :",Ret)
     print("The Addition of obj2 is :",Ret2)

     Ret=obj.Subtraction()
     Ret2=obj.Subtraction()
     print("The Subtraction of obj is :",Ret)
     print("The Subtraction of obj2 is :",Ret2)

     Ret=obj.Multiplication()
     Ret2=obj.Multiplication()
     print("The Multiplication of obj is :",Ret)
     print("The Multiplication of obj2 is :",Ret2)

     Ret=obj.Division()
     Ret2=obj.Division()
     print("The Division of obj is :",Ret)
     print("The Division of obj2 is :",Ret2)


if __name__=="__main__":
     main()    


     




     
     
     


if __name__=="__main__":
     main()


