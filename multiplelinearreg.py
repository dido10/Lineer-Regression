
#multiple linear regression y=b0+b1*x1+b2*x2import pandas as pd
import numpy as mp
from sklearn.linear_model import LinearRegression

df=pd.read_csv("multiple-linear-regression-dataset.csv",sep=";")

x=df.iloc[:,[0,2]].values
y=df.maas.values.reshape(-1,1)

#%% Predict

multiple_linear_reg=LinearRegression()
multiple_linear_reg.fit(x,y)

print("bo:", multiple_linear_reg.intercept_) #x=0 için ilk değer
print("b1,b2", multiple_linear_reg.coef_) 

#A=[[2.5,28]] bu şekilde predict için uygun hale geliyor.
multiple_linear_reg.predict([[2.5,28]])

#♥ bunu nasıl yaptım acaba?? :D
multiple_linear_reg.predict([[2.5,28],[5,30]])
