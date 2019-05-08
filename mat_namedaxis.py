#plot data
import pandas as dd
import matplotlib.pyplot as mt
df = dd.read_csv("linear_reg.csv",sep=";")
mt.scatter(df.yil,df.maas)
mt.xlabel="Deneyim"
mt.ylabel="Maas"
mt.show()
