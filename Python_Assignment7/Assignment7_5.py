def StrX(s):
    left=0
    right=len(s)-1

    while left < right:
        if s[left]!=s[right]:
            return 0
        
        left =left+1
        right=right-1
    return 1
   

def main():
    print("enter the String :")
    Value=input()
    StrX(Value)        

if __name__=="__main__":
    main()
        
