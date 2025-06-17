import schedule
import time
import datetime

def MySchedule():
    print("Inside my schedule function at:",datetime.datetime.now())
def main():
    print("inside automatio script")
    print("Current time is :",datetime.datetime.now())

    schedule.every(20).seconds.do(MySchedule)

    print("end of autonmation script")

if __name__=="__main__":
    main()  