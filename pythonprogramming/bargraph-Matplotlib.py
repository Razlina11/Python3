import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[20,40,100,38,47]
plt.xlim(0,6)
plt.ylim(0,110)
plt.bar(x,y,label=["IBM","AMAZON","GOOGLE","TCS","WIPRO"],color=["Red","Green","Pink","Orange","yellow"],linewidth=1)
plt.xlabel("Company")
plt.ylabel("Statistics")
plt.legend()
plt.show()
