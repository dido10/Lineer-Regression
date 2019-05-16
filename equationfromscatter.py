#lineer denklem- hesaplama
import numpy as np
import pandas as pd
df = pd.read_csv("linear_reg.csv",sep=";")
import matplotlib.pyplot as mt
#sklearn
from sklearn.linear_model import LinearRegression
linear_reg=LinearRegression()
x=df.yil.values.reshape(-1,1)
y=df.maas.values.reshape(-1,1)
linear_reg.fit(x,y)
#bo=y ye x=0 da eşit
b0=linear_reg.predict([[0]])    #b0= [[1107.27496917]]
b0_=linear_reg.intercept_      
print("b0_=",b0_)    #b0_= [1107.27496917]
b1=linear_reg.coef_
print("b1=",b1)#eğim

#sonuç y=1107+1744*X
print(linear_reg.predict([[8.5]]))
array=np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]).reshape(-1,1)
mt.scatter(x,y)
mt.show()
y_head=linear_reg.predict(array)
mt.plot(array,y_head,color="red")# tahmini line çizme 
