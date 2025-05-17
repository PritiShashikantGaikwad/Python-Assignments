def ChkEligibility(Age):
 
    
  if(Age>=18 ):
     
     print("You are eligible for voting") 

  else:
      
      print("You are not  eligible for voting") 



def main():
    print("Enter the Age :")
    Value=int(input())
    ChkEligibility(Value)
   
if __name__=="__main__":
    main() 