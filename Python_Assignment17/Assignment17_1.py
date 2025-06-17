import schedule
import os
import time
import datetime
def Display():
    print("Jay Ganesh..")


def main():
    print("inside autoscript:")
    print("Currect time in main function:",datetime.datetime.now())

    schedule.every(2).seconds.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()
    