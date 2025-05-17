def AreaPerimeter(length,width):
  area=0
  area=length*width
  perimeter=0
  perimeter=2*(length+width)

  return area,perimeter

 
    
  



def main():
    print("Enter the  length :")
    Value=int(input())
    print("Enter the  width :")
    Value2=int(input())
    ret,ret2=AreaPerimeter(Value,Value2)

    print("Area of rectangle is:",ret)
    print("perimeter of rectangle is:",ret2)
   
if __name__=="__main__":
    main() 