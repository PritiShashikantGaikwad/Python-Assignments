import pandas as pd
import matplotlib.pyplot as plt

df=pd.DataFrame({'Name':['Amit','Sagar','pooja'],
          'Math':[85,90,78],
          'Science':[92,88,80],
          'English':[75,85,82]
   
          })
df['Total']=df['Math']+df['Science']+df['English']
df.drop('English')
print(df)
