import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler





data=pd.DataFrame({'Age':[18,22,25,30,35]})
scaler=MinMaxScaler()
scaled_data=scaler.fit_transform(data)
print(scaled_data)























