def Arithematic(No1,No2):
    

    Add=No1+No2
   
    sub=No1-No2
  
    mul=No1*No2

    div=No1/No2
    return Add,sub,mul,div

def main():
    print("Enter the first number:")
    Value1=int(input())
    print("Enter the second number:")
    Value2=int(input())

    ret,ret2,ret3,ret4=Arithematic(Value1,Value2)
    print("The Addition is:",ret)
    print("The subtraction is:",ret2)
    print("The multiplication is:",ret3)
    print("the division is:",ret4)

if __name__=="__main__":
    main()    


