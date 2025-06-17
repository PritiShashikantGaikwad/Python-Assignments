import os
import sys
import shutil
def CopyDir(DirName,DirectoryName):
    flag = os.path.isabs(DirName)

    if(flag == False):
        DirName = os.path.abspath(DirName)

    flag = os.path.exists(DirName)

    if(flag == False):
        print("The path is invalid")
        exit()

    flag = os.path.isdir(DirName)

    if(flag == False):
        print("Path is valid but the target is not a directory")
        exit()
    os.mkdir(DirectoryName)

   

    for  FolderName,SubFolders,FileNames in os.walk(DirName):
        print("Folder Name:"+FolderName)
        for fname in FileNames:
            shutil.copy(os.path.join(FolderName,fname),DirectoryName)
    
   
       



def main():
    
   CopyDir(sys.argv[1],sys.argv[2])

       


   
    
         
if __name__=="__main__":
    main()