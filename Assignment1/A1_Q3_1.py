import numpy as np
from matplotlib import pyplot as plt
from scipy import interpolate

x=np.linspace(-np.pi/2,np.pi/2,11)
y=np.cos(x)

xx=np.linspace(x[0],x[-1],2001)     #cubic spline fit
yy_true=np.cos(xx)
spln=interpolate.splrep(x,y)
yy=interpolate.splev(xx,spln)
plt.clf();
plt.plot(x,y,'*', label="Data")
plt.plot(xx,yy, label="Interpolation")
plt.plot(xx,yy_true, label="True")
plt.title('Cubic Spline cos(x)')
plt.legend(loc='upper left')
plt.savefig('spline_cos.png')
print('my spline rms error is ',np.std(yy-yy_true))

#NEW INTERP METHOD

xi=np.linspace(-np.pi/2,np.pi/2,11)
yi=np.cos(xi)

x=np.linspace(xi[1],xi[-2],1001)       #cubic polynomial interpolation fit
y_true=np.cos(x)
y_interp=np.zeros(len(x))
for i in range(len(x)):    
    ind=np.max(np.where(x[i]>=xi)[0])
    x_use=xi[ind-1:ind+3]
    y_use=yi[ind-1:ind+3]
    pars=np.polyfit(x_use,y_use,3)
    pred=np.polyval(pars,x[i])
    y_interp[i]=pred

plt.clf()
plt.plot(xi,yi,'*',label="Data")
plt.plot(x,y_interp,label="Interpolation")
plt.plot(x,y_true,label="True")
plt.title('Cubic Poly cos(x)')
plt.legend(loc='upper left')
plt.savefig('cubic_cos.png')
print('my cubic poly rms error is ',np.std(y_interp-y_true))