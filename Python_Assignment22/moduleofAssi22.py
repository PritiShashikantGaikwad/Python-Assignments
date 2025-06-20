
import hashlib
import smtplib
import time
import os

import sys
import time

def CalculateChecksum(FileName,bytesize=1024):
   fobj=open(FileName,"rb")
   hobj=hashlib.md5()
   buffer=fobj.read(bytesize)

   while(len(buffer)>0):
      hobj.update(buffer)
      buffer=fobj.read(bytesize)
   fobj.close()
   return hobj.hexdigest()
import os
def FindDuplicate(DirectoryName = "Marvellous"):

    flag = os.path.isabs(DirectoryName)

    if(flag == False):
        DirectoryName = os.path.abspath(DirectoryName)

    flag = os.path.exists(DirectoryName)

    if(flag == False):
        print("The path is invalid")
        exit()

    flag = os.path.isdir(DirectoryName)

    if(flag == False):
        print("Path is valid but the target is not a directory")
        exit()

    Duplicate = {}

    for FolderName , SubFolderNames, FileNames in os.walk(DirectoryName):
        for fname in FileNames:
            fname = os.path.join(FolderName,fname)
            checksum = CalculateChecksum(fname)

            if checksum in Duplicate:
                Duplicate[checksum].append(fname)
            else:
                Duplicate[checksum] = [fname]

    return Duplicate

def DisplayResult(MyDict):
    Result = list(filter(lambda x : len(x) > 1, MyDict.values()))

    Count = 0

    for value in Result:
        for subvalue in value:
            Count = Count + 1
            print(subvalue)
        print("-------------------------------")
        print("Value of Count is : ",Count)
        print("-------------------------------")
        Count = 0

def DeleteDuplicate(Path = "Marvellous"):

    MyDict = FindDuplicate(Path)
    Result = list(filter(lambda x : len(x) > 1, MyDict.values()))

    Count = 0
    Cnt = 0

    for value in Result:
        for subvalue in value:
            Count = Count + 1
            if(Count > 1):
                
                print("Deleted file : ",subvalue)
                copyvalue=subvalue
                
                os.remove(subvalue)
                Cnt = Cnt + 1
        Count = 0

    
    timestamp = time.ctime()
    DirNAme="MarvellousLogDir"
    if not os.path.exists(DirNAme):
        os.mkdir(DirNAme)

    filename = "MarvellousLog%s.log" %(timestamp)
    filename = filename.replace(" ","_")
    filename = filename.replace(":","_")
    filename=os.path.join(DirNAme,filename)

    fobj = open(filename,"w")

    Border = "-"*54
    
    fobj.write(Border+"\n")
    fobj.write("This is a log file of Marvellous Automation Script\n")
    fobj.write("This is a Driectory Cleaner Script\n")
    
    fobj.write("Total deleted file : "+str(Cnt))
  


    fobj.write(Border+"\n")

    fobj.write(Border+"\n")
    fobj.write("This is is created at \n"+timestamp+"\n")
    fobj.write(Border+"\n")
    fobj.close()
    mailSender(filename)


def mailSender(FileName):
    password="axvrfryhu"
    send_from="priti1724@gmail.com"
    to=['www.snehakumawat1731@gmail.com']
    SUBJECT="first pdf through  automail"
    Text="hello sneha"
    Att=open(FileName,"r")
    message='Subject:{}\n\n\n{}\n\n{}'.format(SUBJECT,Text,Att)

    try:
        server=smtplib.SMTP_SSL('smtp.gamil.com',465)
        server.ehlo()
        server.login(send_from,password)
        server.sendmail(send_from,to,message)

        server.close()
        print("Mail sent sucessfully")
    except Exception as e:
        print(e)
        print("unable to send")