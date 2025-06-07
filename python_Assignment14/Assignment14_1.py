class Employee:
    def __init__(self,name,Emp_id,salary):
        self.name=name
        self.Emp_id=Emp_id
        self.salary=salary

    def Display(self):
        print("Name:"+self.name,"ID:",self.Emp_id,"Salary:",self.salary)


def main():
    eobj=Employee("Rohit",101,50000)
    eobj.Display()
        
if __name__=="__main__":
    main()