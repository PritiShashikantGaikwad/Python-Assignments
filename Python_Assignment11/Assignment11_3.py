iSum=0
def Display(No):
    global iSum
    if(No !=0):
        iSum=iSum+No%10
        No=No//10
        Display(No)
    return iSum 


def main():
   Ret= Display(1234)
   print("Sum of digit is:",Ret)


if __name__=="__main__":
    main()


