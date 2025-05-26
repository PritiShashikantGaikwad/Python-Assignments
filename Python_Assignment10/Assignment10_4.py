from functools import reduce

ChkEven=lambda No:No%2==0

Add=lambda No:No**2

Sum=lambda No,No2:No+No2


def main():
    data=[5,2,3,4,3,4,1,2,8,10]
    fdata=list(filter(ChkEven,data))
    print("Data from filter:",fdata)

    mData=list(map(Add,fdata))
    print("The data using map:",mData)

    rData=reduce(Sum,mData)
    print("The data using reduce:",rData)


if __name__=="__main__":
    main()