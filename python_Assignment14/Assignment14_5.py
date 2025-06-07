class BankAccount:
    def __init__(self,Account_no,name,balance):
        self.Account_no=Account_no
        self.name=name
        self.balance=balance

    def deposite(self,amout):
        
        self.balance=self.balance+amout
    def withdraw(self,amout):
        self.balance=self.balance-amout

    def Display(self):
        print(self.balance)


def main():
    obj=BankAccount(101,"priti",23000)
    obj.deposite(90000)
    obj.withdraw(45000)
    obj.Display()

    obj2=BankAccount(102,"vivek",230000)
    obj2.deposite(90000)
    obj2.withdraw(40000)
    obj2.Display()


if __name__=="__main__":
    main()

