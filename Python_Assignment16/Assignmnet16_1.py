import os

def StudentFile(FileName):
    fobj=open(FileName,"w")

    for i in range(5):
        fobj.write()


def main():
    print("Enter the  name of file:")
    Value=input()

    StudentFile(Value)


if __name__=="__main__":
    main()    

