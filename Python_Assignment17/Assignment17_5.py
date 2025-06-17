
import schedule

import time
import datetime


def CurrentimeToFile():
    print("inside automationscript:")
    fobj=open("Marvellous.txt","w")
    
    fobj.write(str(datetime.datetime.now()))
    fobj.close()

   

def main():
   
     
     schedule.every(10).seconds.do(CurrentimeToFile)
     while True:
        schedule.run_pending()
        time.sleep(1)

     
    

if __name__=="__main__":
    main()
