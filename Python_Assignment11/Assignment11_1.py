i=0
def Display(No):
    global i
    if(No>=i):
        print(i)
        i=i+1
       
        Display(No)


def main():
    Display(20)
if __name__=="__main__":    
    main()



    







