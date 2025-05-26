from functools import reduce

ChkNumber=lambda No:(No>=70 and No<=90)

Add=lambda No:No+10

Sum=lambda No,No2:No*No2


def main():
    data=[4,34,36,76,68,24,89,23,86,90,45,70]
    fdata=list(filter(ChkNumber,data))
    print("Data from filter:",fdata)

    mData=list(map(Add,fdata))
    print("The data using map:",mData)

    rData=reduce(Sum,mData)
    print("The data using reduce:",rData)


if __name__=="__main__":
    main()