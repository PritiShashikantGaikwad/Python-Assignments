Power=lambda No:No**2

def main():
    print("Enter the number:")
    value=int(input())
    ret=Power(value)
    print("The power of",value,"is",ret)

if __name__=="__main__":
    main()    