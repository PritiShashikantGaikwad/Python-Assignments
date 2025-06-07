class BookStore:
    NOofBooks=0
    def __init__(self,Name,Author):

        self.Name=Name
        self.Author=Author
        BookStore.NOofBooks=BookStore.NOofBooks+1

    def Display(self):
        print("Name of Book:"+self.Name)
        print("Author of book:"+self.Author)  
        print("Number of books:",BookStore.NOofBooks)  
    


def main():
    obj1=BookStore("Linux System Programming","Robert Love")
    obj1.Display()

    obj2=BookStore("c Programming ","Dennis Rotchie")
    obj2.Display()


if __name__=="__main__":
    main()    
