iSum=0
i=1

def Display(No):
    global iSum,i
   
    if(i<=No):
        iSum=iSum+i
        i=i+1
        Display(No)
    return iSum


def main():
   Ret= Display(5)
   print(Ret)

if __name__=="__main__":
    main()   
        
