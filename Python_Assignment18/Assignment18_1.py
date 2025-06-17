import os
def CkeckFileExists(FileName):
    Ret=os.path.exists(FileName)

    if(Ret==True):
        print("The file is Exists:"+FileName)
    else:
        print("The file is not exists:"+FileName)

def main():
    print("Enter the filename")
    FileName=input()
    CkeckFileExists(FileName)

if __name__=="__main__":
    main()
