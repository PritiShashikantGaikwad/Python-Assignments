def add(no):
    return no*2

def main():
      Data=[]
      print("Enter the number of elements:")
      size=int(input())
      print("Enter the elements")
      for i in range(size):
           no=int(input())
           Data.append(no)
      MData=list(map(add,Data))
      print("Data from Map:",MData)

if __name__=="__main__":
     main()      
