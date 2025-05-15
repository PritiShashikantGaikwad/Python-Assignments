Multiplication=lambda No1,No2: No1*No2

def main():
    print("Enter the first Number:")
    value1=int(input())
    print("Enter the second Number:")
    value2=int(input())
    Ret=Multiplication(value1,value2)
    print("the multiplication is",Ret)

if __name__=="__main__":
    main()