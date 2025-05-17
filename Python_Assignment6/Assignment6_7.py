def ChkLarge(No1,No2,No3,No4,No5):
   if(No1>No2 and No1>No3 and No1>No4 and No1>No5):
       print("The first number is greater:",No1)

   elif(No2>No1 and No2>No3 and No2>No4 and No2>No5):   
       print("The Second number is greater : ",No2)

   elif(No3>No1 and No3>No2 and No3>No4 and No3>No5):   
       print("The Third number is greater : ",No3)

   elif(No4>No1 and No4>No2 and No4>No3 and No4>No5):   
       print("The Fourth number is greater : ",No4)
       
   else:
       print("The Fifth number is greater",No5)    
            

            

         

def main():
    print("Enter the 1 st number:")
    Value=int(input())
    
    print("Enter the  2 nd number:")
    Value2=int(input())
    
    print("Enter the  3 rd number:")
    Value3=int(input())
  
    print("Enter the  4 th number:")
    Value4=int(input())
    
    print("Enter the 5 th  number:")
    Value5=int(input())
    ChkLarge(Value,Value2,Value3,Value4,Value5) 
  
    

if __name__=="__main__":
    main()