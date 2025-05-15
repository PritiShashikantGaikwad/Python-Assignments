def Display(iRow,iCol):

    for i in range(iRow):
        for j in range(iCol):
            print("*", end="\t")
        print()       
      



def main():
    print("Enter the row:")
    value1=int(input())
    print("Enter Column:")
    value2=int(input())

    Display(value1,value2)

if __name__=="__main__":
    main()