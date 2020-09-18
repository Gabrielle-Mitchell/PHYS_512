import numpy as np
from matplotlib import pyplot as plt
from scipy import interpolate
data = np.loadtxt(".\Desktop\PHYS_512\Ass1\lakeshore.txt") 
#print(data)
#print("shape of data:",data.shape)
data1 = data[:144, :2]
#print(data1)
#print("shape of data1:",data1.shape)

y=data1[:, 1]
x=data1[:, 0]
#print(x)
#print("shape of x:",x.shape)
#print(y)
#print("shape of y:",y.shape)


xx=np.linspace(x[0],x[-1],2001)
x3=x[0::2]    #make larger step sizes to estimate error afterwards
y3=y[0::2]
#print(x3)
#print(y3)

spln=interpolate.splrep(x,y)    #splines
yy=interpolate.splev(xx,spln)
spln2=interpolate.splrep(x3,y3)    #splines with larger step size
yy2=interpolate.splev(xx,spln2)
plt.clf();
plt.plot(x,y,'.',label="Data")
plt.plot(xx,yy,label="Interpolation")
plt.title('Lakeshore Diodes')
plt.xlabel('Temperature')
plt.ylabel('Voltage')
plt.legend(loc='upper left')
plt.savefig('lakeshore_out.png')
print('my error estimate is ',np.amax(np.abs(yy-yy2)))

