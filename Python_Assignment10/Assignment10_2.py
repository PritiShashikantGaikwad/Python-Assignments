Multiplication=lambda No,No2:No*No2

def main():
    print("Enter the 1 st  number:")
    value=int(input())
    print("Enter the  2 nd number:")
    value2=int(input())
    ret=Multiplication(value,value2)
    print("The Multiplication is:",ret)

if __name__=="__main__":
    main()    