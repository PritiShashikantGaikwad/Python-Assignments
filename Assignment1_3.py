def Add(iNo1,iNo2):
   
   ans=iNo1+iNo2
   return ans


def main():
    print("Enter the  first number:")
    iValue1=int(input())

    print("Enter the  second number:")
    iValue2=int(input())

    iRet =Add(iValue1,iValue2)
    print("The addition is:",iRet)

if __name__=="__main__":
    main() 