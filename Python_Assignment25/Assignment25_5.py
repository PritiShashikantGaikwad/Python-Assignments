import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

from sklearn.preprocessing import LabelEncoder

data=pd.DataFrame({'Age':[22,25,47,52,46,56],'Purchase':[0,1,1,0,1,0]})

x=data.drop('Purchase',axis='columns')
y=data['Purchase']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

















