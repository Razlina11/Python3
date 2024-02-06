import numpy as np
import matplotlib.pyplot as plt
def linereg(x,y):
    a=np.size(x)
    mnx=np.mean(x)
    mny=np.mean(y)
    cd=np.sum((y*x))-a*mny*mnx
    dx=np.sum((x*x))-a*mnx*mnx
    r1=cd/dx
    r0=mny-r1*mnx
    print("Coefficients:r0=",r0,"r1=",r1)
    plt.scatter(x,y,color='r',label="observation points")
    pred=r0+r1*x
    plt.plot(x,pred,color="black",label="Regression line")
    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    plt.legend()
    plt.show()


x=np.array([0,1,2,3,4,5,6,7,8,9])
y=np.array([1,3,2,5,7,8,8,9,10,12])
linereg(x,y)
