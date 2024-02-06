import matplotlib.pyplot as plt
x1=[2,4,6,8]
y1=[1,3,5,7]
plt.plot(x1,y1,label="line A",color="black")
x2=[3,6,9,12]
y2=[4,8,12,16]
plt.plot(x2,y2,label="line B",color="green")
plt.xlim(0,12)
plt.ylim(0,12)
plt.xlabel("X-AXIS")
plt.ylabel("Y-AXIS")
plt.legend()
plt.show()
