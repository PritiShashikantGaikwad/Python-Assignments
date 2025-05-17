def Factorial(No):
    fact=1
    for i in range(1,No):
        fact=fact*i
    return fact    

         

def main():
    print("Enter the number:")
    Value=int(input())
    ret=Factorial(Value) 
    print("Factorial is :",ret)
    

if __name__=="__main__":
    main()