import pandas as pd
from sklearn.preprocessing import StandardScaler,MinMaxScaler


df=pd.DataFrame({'Name':['Amit','Sagar','pooja'],
          'Math':[85,90,78],
          'Science':[92,88,80],
          'English':[75,85,82]
          })
print(df)
data=['Male','Male','Female']
df['Gender']=data

#encoded_df=pd.get_dummies(df,columns=['Gender'])
#print(encoded_df)

df['Gender']=df['Gender'].map({'Female':0,'Male':1})
print(df)



    

