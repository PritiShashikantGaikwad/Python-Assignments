def MultiTable(No):
    iSum=0
    for i in range(1,11):
      print(No*i)

         

def main():
    print("Enter the number:")
    Value=int(input())
    MultiTable(Value) 
    

if __name__=="__main__":
    main()