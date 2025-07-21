import numpy as np
import pandas as pd



data=pd.DataFrame({'Grade':['A+','B','A','C','B+']})
replace_dist={'A+':'Excellent','A':'Very Good','B+':'Good','B':'Average','C':'Poor'}

data=data.replace(replace_dist)
print(data)



















