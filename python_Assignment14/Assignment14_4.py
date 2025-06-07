class Student:
    School_name="Modern"
    def __init__(self,name,rollno):

      self.name=name
      self.rollno=rollno

    def Display(self):
       print("name:"+self.name)
       print("roll no:",self.rollno)
       print("School name:"+Student.School_name)

def main():

   obj=Student("priti",123)
   obj.Display()
   Student.School_name="Marvellous"
   print("after changing name:"+Student.School_name)

if __name__=="__main__":
   main()   
   

