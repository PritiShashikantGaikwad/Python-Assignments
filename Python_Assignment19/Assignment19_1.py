import os


def main():
    print("Enter the directory name:")
    DirName=input()
    print("Enter the extension")
    exten=input()

   
    flag = os.path.isabs(DirName)

    if(flag == False):
        DirectoryName = os.path.abspath(DirName)

    flag = os.path.exists(DirName)

    if(flag == False):
        print("The path is invalid")
        exit()

    flag = os.path.isdir(DirName)

    if(flag == False):
        print("Path is valid but the target is not a directory")
        exit()

   

    for  FolderName,SubFolders,FileNames in os.walk(DirName):
        print("Folder Name:"+FolderName)
        for fname in FileNames:
            if(fname.endswith(exten)):
                print(fname)

         
if __name__=="__main__":
    main()