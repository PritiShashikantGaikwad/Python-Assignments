import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
data=pd.DataFrame({'City':['Pune','Mumbai','Delhi','Pune','Delhi']})


le=LabelEncoder()

encoded_data=le.fit_transform(data['City'])

print("Coded data:",encoded_data)









