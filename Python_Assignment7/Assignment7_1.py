Square=lambda No: No**2
Cube=lambda No: No**3

def main():
    print("Enetr the number:")
    value=int(input())
    ret=Square(value)
    ret2=Cube(value)
    print("Square:",ret)
    print("Cube:",ret2)

if __name__=="__main__":
    main()    
