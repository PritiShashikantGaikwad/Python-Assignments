import MarvellousNum as A

def main():
        Data=[]
        print("enter the no of element u want to enter :")
        Value=int(input())

        print("Enter the Array elements:")
        for i in range(Value):
              no=int(input())
              Data.append(no)
        Ret=A.ChkPrime(Data)  
        print("The ADDITON IS :",Ret)    


if __name__=="__main__":
    main()    