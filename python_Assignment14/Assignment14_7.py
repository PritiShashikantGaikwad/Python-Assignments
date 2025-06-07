class Person:
    def __init__(self,name,age):
       self.name=name
       self.age=age

    def Display(self):
        print("Name:"+self.name,"Age:",self.age)  

class Teacher(Person):
    def __init__(self, name, age,subject,salary):
        super().__init__(name, age)  
        self.subject=subject
        self.salary=salary

    def Display(self):
         super().Display() 
         print("Subject is:"+self.subject) 
         print("Salry is:",self.salary)

def main():
    obj=Teacher("priti",21,"Maths",200000)
    obj.Display()

if __name__=="__main__":
    main()    