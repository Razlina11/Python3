import numpy as np
import matplotlib.pyplot as plt
x=np.random.randn(50)
y1=x*5+3
y2=-5*x
y3=np.random.randn(50)
plt.scatter(x,y1,color="red",label=f"Positive corr coeff={np.round(np.corrcoef(x,y1)[0,1],1)}")
plt.scatter(x,y2,color="black",label=f"Negative corr coeff={np.round(np.corrcoef(x,y1)[0,1],2)}")
plt.scatter(x,y3,color="pink",label=f"Zero corr coeff={np.round(np.corrcoef(x,y1)[0,1],3)}")
plt.rcParams.update({'figure.figsize':(10,8),'figure.dpi':100})
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.legend()
plt.show()
