
#multiple linear regression y=b0+b1*x1+b2*x2
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
df=pd.read_csv("regressiondataset.csv",sep=";")
y=df.maas.values.reshape(-1,1)
x=df.iloc[:,[0,2]].values

multiplereg=LinearRegression()
multiplereg.fit(x,y)

print("b0:",multiplereg.intercept_)
print("b1 and b2 :",multiplereg.coef_)


multiplereg.predict(np.array([[2,27],[15,48]]))

