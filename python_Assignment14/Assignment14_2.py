class Rectangle:
    def  __init__(self,length,width):
       self.length=length
       self.width=width

    def Area(self):
        Ans=0
        Ans=self.length*self.width
        return Ans

    def Perimeter(self):
        ans=0
        ans=2*(self.length+self.width)  
        return ans   

def main():
    obj=Rectangle(20,30)
    obj2=Rectangle(40,50)
    Ret=obj.Area()
    print("Are of Rectangle is:",Ret)
    Ret2=obj.Perimeter()
    print("perimeter  of Rectangle is:",Ret2)

    Ret=obj2.Area()
    print("Are of Rectangle is:",Ret)
    Ret2=obj2.Perimeter()
    print("perimeter  of Rectangle is:",Ret2)

if __name__=="__main__":
    main()    
