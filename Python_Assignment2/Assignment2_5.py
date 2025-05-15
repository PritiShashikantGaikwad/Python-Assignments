def DisplayPrime(No):
  
  iCnt=0
  
  ret=False
  for i in range (1,No):
    if  (No % i ==0):
      iCnt=iCnt+1


  if(iCnt>2):
    ret=True
    
   

  

def main():
  bRet=False
  print("Enter the number")
  value=int(input())
  bRet=DisplayPrime(value)

  if(bRet==True):
    print("The number is not prime")

  else:
    print("The no is prime number")  
  


if __name__=="__main__":
   main()