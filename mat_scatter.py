#  noktasal data görünüm
#manuel data import edilecek--variable explorer 

import pandas as pd
import numpy as np
df = pd.DataFrame(randm100_3csv,columns=["yil","maas","def"])
import matplotlib.pyplot as mt
mt.scatter(df.yil,df.maas)
