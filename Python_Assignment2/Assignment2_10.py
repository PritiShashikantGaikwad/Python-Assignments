def Sum(No):
    iSUm=0
  
    while(No!=0):
        Digit=No %  10
        iSUm=iSUm+Digit
        No=No/10

    return iSUm 

  
    

  

def main():
  print("Enter the number")
  value=int(input())
  Ret=Sum(value)
  print("Addition is    ",Ret)


if __name__=="__main__":
   main()