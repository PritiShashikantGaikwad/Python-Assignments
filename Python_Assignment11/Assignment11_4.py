"""i=0
power=0
def Display(No):
    global i,power
    if(i<=No):
        power= 2*2
        i=i+1
    Display(No)    
    return power

def main():
    Ret=Display(3)
    print("power is:",Ret)

if __name__=="__main__":
    main() """   

