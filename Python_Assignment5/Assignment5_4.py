def ChkLarge(no1,no2,no3):
 
    
  if(no1>no2 and no1>no3):
     
     print("First number is greater:",no1) 

  elif (no2>no1 and no2>no3):
      
      print("second number is greater:",no2)
  else:
     print("the third number is greater",no3)     



def main():
    print("Enter the first number :")
    Value=int(input())
    print("Enter the second number :")
    Value2=int(input())
    print("Enter the third number :")
    Value3=int(input())
    
    ChkLarge(Value,Value2,Value3)
   
if __name__=="__main__":
    main() 