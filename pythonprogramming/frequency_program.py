import numpy as np
import pandas as pd
def interval():
    iv=["1-3","4-6","7-9","Total"]
    return iv
def frequency():
    k=len(a1)+len(a2)+len(a3)
    f=[len(a1),len(a2),len(a3),k]
    return f



a=[1,2,3,2,6,7,6,6,8,9]
y=np.sort(a)
a1=[]
a2=[]
a3=[]
for i in y:
    if i>=1  and i<=3:
        a1.append(i)
    elif i>=4 and i<=6:
        a2.append(i)
    elif i>=7 and i<=9:
        a3.append(i)

data=[a1,a2,a3]
z=interval()
f=frequency()
s=pd.DataFrame(zip(z,f),columns=["Interval","Frequency"],index=['a','b','c','d'])
print(s)
