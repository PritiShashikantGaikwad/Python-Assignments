import os
def CheckFileExists(FileName):
    
    ret=os.path.exists(FileName)

    if(ret==True):
        print("The file is exists:")
    else:
        print("The file is not exists:")

def main():
    print("Enter the file name :")
    Value=input()

    CheckFileExists(Value)


if __name__=="__main__":
    main()



