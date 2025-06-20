import schedule
import moduleofAssi22 as a
import sys
import time




   


def main():
    Border = "-"*54
    print(Border)
    print("--------------- Marvellous Automation ----------------")
    print(Border)

    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to perform directory cleaning")
            print("This is the directory automation script")

        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as ")
            print("ScriptName.py  NameOfDirctory timeinterval")
            print("Please provide valid absolute path")

    if(len(sys.argv) == 3):
            schedule.every(int(sys.argv[2])).minutes.do(a.DeleteDuplicate)

            while True:
                schedule.run_pending()
                time.sleep(1)

    else:
        print("Invalid number of coomand line arguments")
        print("Use the given flags as : ")
        print("--h : Used to display the help")
        print("--u : Used to display the usage") 

    print(Border)
    print("----------- Thank you for using our script -----------")
    print("---------------- Marvellous Infosystems --------------")
    print(Border)
    
if __name__=="__main__":
   
   main()
   