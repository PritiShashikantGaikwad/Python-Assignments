import schedule
import os
import time
import datetime
def Display():
  print("Do Coding ...!")


def main():
    print("inside autoscript:")
  

    schedule.every(30).minutes.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()