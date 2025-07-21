import numpy as np
import pandas as pd






data=pd.DataFrame({'marks':[85,np.nan,90,np.nan,95]})

data_new=data.interpolate()
print(data_new)























