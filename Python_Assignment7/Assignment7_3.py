def ChkEven(no):
    return (no %2==0)

def main():
      Data=[]
      print("Enter the number of elements:")
      size=int(input())
      print("Enter the elements")
      for i in range(size):
           no=int(input())
           Data.append(no)

          
      MData=list(filter(ChkEven,Data))
      print("Data from Filter:",MData)

if __name__=="__main__":
     main()    