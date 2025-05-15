def DisplayFact(No):
    iCnt=0
  
    while(No!=0):
      
        iCnt+=1
        No=No/10

    return iCnt 

  
    

  

def main():
  print("Enter the number")
  value=int(input())
  Ret=DisplayFact(value)
  print("Count   ",Ret)


if __name__=="__main__":
   main()