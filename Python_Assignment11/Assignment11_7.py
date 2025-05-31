"""i=0
j=0

def Display(iRow,iCol):
        global i,j
        if(i<=iRow):
            if(j<=iCol):
                print("*",end=" ")
                j=j+1
            i=i+1 
        Display(iRow,iCol)       
        print()        

def main():
    Display(4,4)


if __name__=="__main__":
    main()"""
