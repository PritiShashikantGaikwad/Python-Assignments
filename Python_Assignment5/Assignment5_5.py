def ChkEvenOdd(no1):
 
    
  if(no1 %2==0):
     
     print("The number is Even") 


  else:
     print("the  number is Odd")     



def main():
    print("Enter the  number :")
    Value=int(input())
    ChkEvenOdd(Value)
   
if __name__=="__main__":
    main() 