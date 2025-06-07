class BankAccount:
    ROI=10.5

    def __init__(self,Name,Amount):
        self.Name=Name
        self.Amount=Amount
   
        
    def Deposite(self,Amt):
       
        self.Amount=self.Amount+Amt
        

    def Withdraw(self,amt):
       self.Amount=self.Amount-amt  
        

    def CalculateInterest(self,Amt):
        ans=(BankAccount.ROI*100)/Amt
        return ans
    def Display(self):
        print("the name of bank:"+self.Name)
        print("the Amount is:",self.Amount)


def main():
  obj=BankAccount("SBI",12000)
  obj.Deposite(12000)
  obj.Withdraw(6000)
  Ret=obj.CalculateInterest(3400)
  print("Rate of interest is:",Ret)
  obj.Display()

  obj2=BankAccount("BOB",40000)
  obj2.Deposite(3000)
  obj2.Withdraw(2000)
  Ret2=obj2.CalculateInterest(3400)
  print("Rate of interest is:",Ret2)
  obj2.Display()

if __name__=="__main__":
    main()