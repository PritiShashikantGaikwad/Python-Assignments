def ChkNum(iNo):
    if(iNo % 2 ==0):
        print("Even Number")
    else:
        print("Odd Number")  


def main():
    print("Enter the number:")
    iValue=int(input())

    ChkNum(iValue)

if __name__=="__main__":
    main()    

