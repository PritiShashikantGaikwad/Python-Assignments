import numpy as np
import pandas as pd
data=pd.DataFrame({'Name':['A','B','C'],'Age':[12.0,22.0,23.0]})





Covert_data={'Age':int}
data=data.astype(Covert_data)
print(data.dtypes)




