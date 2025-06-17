import hashlib
import os
import sys
def calculateCheckSum(FileName,BlockSize=1024):
             fobj=open(FileName,"rb")
             hobj=hashlib.md5()
             buffer=fobj.read(BlockSize)
             while(len(buffer)>0):
                    hobj.update(buffer)
                    buffer=fobj.read(BlockSize)
             fobj.close() 
             return hobj.hexdigest()       


def CheckSumOfFiles(DirName):

    for FolderName,SubFolderName,FileNames in os.walk(DirName):
        print("Directory Name:"+FolderName)
        for fname in FileNames:
               cheksum=os.path.join(FolderName,fname)
               ret=calculateCheckSum(cheksum)
               print("FileName:"+fname)
               print("CheckSum of File is",ret)
           


def main():
       CheckSumOfFiles(sys.argv[1])

if __name__=="__main__":
       main()
    

