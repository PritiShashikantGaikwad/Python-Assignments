Power=lambda No: No**2

def main():
    print("Enter the Number:")
    value=int(input())
    Ret=Power(value)
    print("the square root of ",value,"is",Ret)

if __name__=="__main__":
    main()    