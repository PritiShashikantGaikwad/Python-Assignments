class Circle:
    PI=3.14
    def __init__(self):
          print("inside constructor:")
          self.Radius=0.0
          self.Area=0.0
          self.Circumference=0.0

    def Accept(self):
         print("Emter the value for radius:")
         self.Radius=float(input())

    def CalculateArea(self):
         self.Area=self.Radius*self.Radius*Circle.PI

    def CalculateCircumference(self):
            self.Circumference=2*self.Radius*Circle.PI

    def Display(self):
          print("Area of circle:",self.Area) 
          print("Radius of circle:",self.Radius)
          print("Circumference of circle:",self.Circumference)   

def main():
      obj1=Circle()
      obj2=Circle()

      obj1.Accept()
      obj2.Accept()

      obj1.CalculateArea()
      obj2.CalculateArea()

      obj1.CalculateCircumference()
      obj2.CalculateCircumference()

      obj1.Display()
      obj2.Display()



if __name__=="__main__":
      main()
            
               

              
               