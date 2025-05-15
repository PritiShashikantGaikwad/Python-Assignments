def DisplayFact(No):
  iSum=0
  for i in range(1,No):
    iSum=iSum+i

  return iSum 

def main():
  print("Enter the number")
  value=int(input())
  Ret=DisplayFact(value)
  print("Addition  of ",value,"is",Ret)


if __name__=="__main__":
   main()
