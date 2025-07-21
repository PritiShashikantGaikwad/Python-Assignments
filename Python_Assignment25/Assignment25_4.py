import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
data=pd.DataFrame({'City':['Pune','Mumbai','Delhi','Pune','Delhi']})


df_encoding=pd.get_dummies(data['City'],dtype=int)
print(df_encoding)









