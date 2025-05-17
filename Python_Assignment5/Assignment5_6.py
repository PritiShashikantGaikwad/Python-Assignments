def ConvertToFahrenheit(celsius):
    F=((celsius*9/5)+32)
    
    return F



 
    
  



def main():
    print("Enter the  celsius :")
    Value=int(input())
  
    ret=ConvertToFahrenheit(Value)

    print("Temperature in Fahrenheit:",ret,"F")
   
   
if __name__=="__main__":
    main() 