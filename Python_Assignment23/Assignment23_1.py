import pandas as pd

df=pd.DataFrame({'Name':['Amit','Sagar','pooja'],
          'Math':[85,90,78],
          'Science':[92,88,80],
          'English':[75,85,82]
   
          })
print(df)
   
print(df.shape)
print(df.columns)
print(df.dtypes)