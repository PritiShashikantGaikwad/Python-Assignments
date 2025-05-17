def SumOfEven():
    iSum=0
    for i in range(1,101):
        if(i %2 ==0):
            iSum=iSum+i

    return iSum        

def main():
   
    ret=SumOfEven() 
    print("the sum of even number between 1 to 100:",ret)  

if __name__=="__main__":
    main()