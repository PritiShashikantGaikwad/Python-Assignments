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
marks=df[df['Name']=='Sagar'][['Math','Science','English']].values.flatten()
print(marks)
subject=['Math','Science','English']

plt.pie(marks,labels=subject)
plt.title("Simple pie chart")
plt.show()






    

