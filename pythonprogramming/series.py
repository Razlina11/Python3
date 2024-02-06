import pandas as pd
import numpy as np
s=['Arun','Rajesh','Ramesh','Suresh']
d=np.sort(s)
e=pd.Series(d,index=['a','b','c','d'])
#e.index+=1
print(e)
