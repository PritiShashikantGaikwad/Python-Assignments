i=1
def Display(No):
    global i
    if(i<=No):
        if(No%i==0):
            print(i)
        i=i+1
        Display(No)

def main():
    Display(20)

if __name__=="__main__":    
    main()