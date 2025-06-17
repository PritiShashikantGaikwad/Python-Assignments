import os
import sys
import time
import hashlib  #used to calculate checksum

def CalculateCheckSum(path,BlockSize=1024):
     fobj=open(path,"rb")

     hobj=hashlib.md5()

     buffer=fobj.read(BlockSize)

     while(len(buffer)>0):
        hobj.update(buffer)
        buffer=fobj.read(BlockSize)

     fobj.close()
     return hobj.hexdigest()


def DirectoryWatcher(DirectoryName="Marvellous"):
    TotalCnt=0
    EmptyCnt=0
    flag=os.path.isabs(DirectoryName)

    if (flag==False):#updater
        DirectoryName=os.path.abspath(DirectoryName)

    flag =os.path.exists(DirectoryName)

    if(flag==False):#filter
        print("THe path is invalid:")
        exit()  

    flag=os.path.isdir(DirectoryName)
    if(flag==False):
        print("The path is valid but the target is not a directory")      

    print("Absolute path is :"+DirectoryName)
    for FolderName ,SubFolderNames, FileNames in os.walk(DirectoryName):
       for fname in FileNames :
           checksum=os.path.join(FolderName,fname)
           ret=CalculateCheckSum(checksum)
           print("File name",fname)
           print("check sum:",ret)

    
    timestamp=time.ctime()
    FileName="MarvellousLog%s.log" %(timestamp)
    FileName=FileName.replace(" ","_")
    FileName=FileName.replace(":","_")

    
    fobj=open(FileName,"w")

    Border="_"*54

    fobj.write(Border+"\n")#concatination means \n
    fobj.write("This is a log file of marvellous  automation script\n")
    fobj.write("This is a directory cleaner  script\n")
   
    fobj.write(Border)

    fobj.write("\n\n\n\n\n\n\n\n\n\n\n\n\n")
    
    fobj. write(str(TotalCnt))
    fobj. write(str(EmptyCnt))

    fobj.write(Border+"\n")#concatination means \n
    fobj.write("This is  Created at \n"+timestamp+"\n")
    fobj.write(Border)     

def FindDuplicate(DirectoryName="Marvellous"):
   
    flag=os.path.isabs(DirectoryName)

    if (flag==False):#updater
        DirectoryName=os.path.abspath(DirectoryName)

    flag =os.path.exists(DirectoryName)

    if(flag==False):#filter
        print("THe path is invalid:")
        exit()  

    flag=os.path.isdir(DirectoryName)
    if(flag==False):
        print("The path is valid but the target is not a directory")      

    Duplicate={}
    for FolderName ,SubFolderNames, FileNames in os.walk(DirectoryName):
       for fname in FileNames : 
           fname=os.path.join(FolderName,fname)
           checksum=CalculateCheckSum(fname)
           if checksum in Duplicate:
               Duplicate[checksum].append(fname)
           else:
               Duplicate[checksum]=[fname]

    return Duplicate

def DisplayResult(MyDict):
    Result=list(filter(lambda x:len(x)>1,MyDict.values()))
    Count=0
    for Value in Result:
        for Subvalue in Value:
            Count=Count+1
            print(Subvalue)
        print("_______________________________")
        print("value of count is:",Count)
        print("________________________________")
        Count=0



def DeleteDuplicate(MyDict):
    Result=list(filter(lambda x:len(x)>1,MyDict.values()))
    Count=0
    for Value in Result:
        for Subvalue in Value:
            Count=Count+1
            if(Count>1):
                os.remove(Subvalue)
    
       
        Count=0
           
    

def main():
    Border="_"*80
    print(Border)
    print("______________________________ Automations_________________________")
    print(Border)
    #logic
    if(len(sys.argv)==2):
        if((sys.argv[1]=="--h") or (sys.argv[1]=="--H")):
            print("This application is used to performed directory cleaner")
            print("This is the directory  automation script")
        elif((sys.argv[1]=="--u") or (sys.argv[1]=="--U")):  
            print("use the given script  to find the duplicate files from directory   ")
            print("ScriptName.py NameofDirectory ")
            print("please enter valid absolute path")
        else:
          Result=FindDuplicate(sys.argv[1]) 
          DeleteDuplicate(Result)
    else:
        print("invalid number of command line arguments:")
        print("use the given flages as :")

        print("--h:used to display the help")
        print("--u used to dsplay thr usage") 


    


    print(Border)
    print("___________________________Thank you for using our script ______________________")
   
    print(Border)

if __name__=="__main__":
    main()