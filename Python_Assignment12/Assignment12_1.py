class Demo:
    value="10"
    def __init__(self,A,B):
        self.no1=A
        self.no2=B
    def Fun(self):
        print("no1 from Fun method:",self.no1) 
        print("no2 from Fun method:",self.no2)   

    def Gun(self):
         print("no1 from Gun method:",self.no1) 
         print("no2 from Gun method:",self.no2)  

def main():
    print("the class variable is:",Demo.value)
    obj1=Demo(11,21)
    obj2=Demo(51,101)

    obj1.Fun()
    obj2.Fun()
    obj1.Gun()
    obj2.Fun() 

if __name__=="__main__":
    main()

