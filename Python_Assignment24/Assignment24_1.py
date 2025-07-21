import pandas as pd
from sklearn.preprocessing import StandardScaler,MinMaxScaler


def main():
      df=pd.DataFrame({'Name':['Amit','Sagar','pooja'],
          'Math':[85,90,78],
          'Science':[92,88,80],
          'English':[75,85,82]
          })
      data=df['Math'],df['Science'],df['English']
      scaler=MinMaxScaler()
      scalerdata=scaler.fit_transform(data)
      print(scalerdata)


if __name__=="__main__":
    main()