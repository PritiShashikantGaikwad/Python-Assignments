def Display(iNo):

    if(iNo % 5 == 0):
        ans= True
    else:
        ans= False

        return ans


def main():
    print("Enter the number:") 
    iValue=int(input())

    iRet=Display(iValue)
    if(iRet== True):
        print("The number is divisible by 5 ")
    else:
        print("the number is not divisible by 5")  


if __name__=="__main__":
    main()


   
