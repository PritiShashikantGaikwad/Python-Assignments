def ChkPrime(no):
        iCnt=0
        for i in range(1,no):
              
              if (no %i ==0):
                    iCnt=iCnt+1
        if(iCnt<=2):
              return no
                  

def main():
      Data=[]
      print("Enter the number of elements:")
      size=int(input())
      print("Enter the elements")
      for i in range(size):
           no=int(input())
           Data.append(no)

          
      MData=list(filter(ChkPrime,Data))
      print("Data from Filter:",MData)

if __name__=="__main__":
     main()  