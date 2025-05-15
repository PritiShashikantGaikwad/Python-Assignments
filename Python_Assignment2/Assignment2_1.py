import AssignmentModule  
def main():
    print("Enter the first number:")
    value1=int(input())

    print("Enter the second number:")
    value2=int(input())

    Ret=AssignmentModule.Addition(value1,value2)
    print("Addition is :",Ret)

    Ret2=AssignmentModule.Subtract(value1,value2)
    print("Subtract is",Ret2)

    Ret3=AssignmentModule.MUltiplication(value1,value2)
    print("multiplication is:",Ret3)

    Ret4=AssignmentModule.Division(value1,value2)
    print("Division is:",Ret4)


if __name__=="__main__":
    main()    





