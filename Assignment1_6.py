def ChkNum(iNo):
    if(iNo==0):
        print("Zero")
    elif(iNo > 0):
        print("The number is positive")    
    else:   
      print("the number is negative")

def main():
    print("Enter the number:")
    iValue=int(input())

    ChkNum(iValue)

if __name__=="__main__":
    main()    