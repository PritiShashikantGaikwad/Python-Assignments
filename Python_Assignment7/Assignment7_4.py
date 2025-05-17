from functools import reduce

def Sum(no,no2):
    return(no*no2)

def main():
      Data=[]
      print("Enter the number of elements:")
      size=int(input())
      print("Enter the elements")
      for i in range(size):
           no=int(input())
           Data.append(no)

          
      MData=reduce(Sum,Data)
      print("Data from reduce:",MData)

if __name__=="__main__":
     main()  