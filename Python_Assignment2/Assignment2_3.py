def DisplayFact(No):
  Fact=1
  for i in range(1,No):
    Fact=Fact*i

  return Fact 

def main():
  print("Enter the number")
  value=int(input())
  Ret=DisplayFact(value)
  print("Factorila of ",value,"is",Ret)


if __name__=="__main__":
   main()
