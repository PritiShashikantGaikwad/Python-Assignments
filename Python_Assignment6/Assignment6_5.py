def ChkPrime(No):
   icnt=0
   for i in range(1,No):
       if(No %i==0):
           icnt=icnt+1

   if(icnt>2):
       print("the number is not prime:",No)
   else:
       print("the number is prime:",No)    
       
         

def main():
    print("Enter the number:")
    Value=int(input())
    ChkPrime(Value) 
  
    

if __name__=="__main__":
    main()