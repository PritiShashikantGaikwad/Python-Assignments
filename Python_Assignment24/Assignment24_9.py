import pandas as pd
from sklearn.preprocessing import StandardScaler,MinMaxScaler
import matplotlib.pyplot as plt



df=pd.DataFrame({'Name':['Amit','Sagar','pooja'],
          'Math':[85,90,78],
          'Science':[92,88,80],
          'English':[75,85,82]
          })
print(df)
df['Total']=df['Math']+df['Science']+df['English']
data=['Male','Male','Female']
df['Gender']=data
df['Gender']=df['Gender'].map({'Female':0,'Male':1})


df=df.rename(columns={'Math':'Mathematics'})
print(df)






    

