import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.DataFrame({'Name':['Amit','Sagar','pooja'],
          'Math':[np.nan,90,78],
          'Science':[92,np.nan,80]
          
   
          })

df.fillna(df.mean(numeric_only=True),inplace=True)
print(df)

