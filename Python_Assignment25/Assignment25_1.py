import numpy as np
import seaborn as sns
data={'Salary':[25000,27000,29000,31000,50000,100000]}


#Quartiles

"""Quer1=26000
Quer2=75000

#IQR
IQR=75000-26000
print(IQR)

#Outlier fences

LowerF=Quer1-(1.5*IQR)
UpperF=Quer2-(1.5*IQR)

print("Lower Fences:",LowerF)
print("Upper Fences:",UpperF)"""

q1=np.quantile(data["Salary"],0.25)
q2=np.quantile(data["Salary"],0.50)
q3=np.quantile(data["Salary"],0.75)

print("Quartile smaller:",q1)
print("Quartile medium :",q2)
print("Quartile higher:",q3)

IQR=q3-q1
LowerF=q1-(1.5*IQR)
UpperF=q2-(1.5*IQR)
print("Lower Fences:",LowerF)
print("Upper Fences:",UpperF)



