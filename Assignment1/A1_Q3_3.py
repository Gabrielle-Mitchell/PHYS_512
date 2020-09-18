import numpy as np
from matplotlib import pyplot as plt

def rat_eval(p,q,x):
    top=0
    for i in range(len(p)):
        top=top+p[i]*x**i
    bot=1
    for i in range(len(q)):
        bot=bot+q[i]*x**(i+1)
    return top/bot

def rat_fit(x,y,n,m):
    assert(len(x)==n+m-1)
    assert(len(y)==len(x))
    mat=np.zeros([n+m-1,n+m-1])
    for i in range(n):
        mat[:,i]=x**i
    for i in range(1,m):
        mat[:,i-1+n]=-y*x**i
    #pars=np.dot(np.linalg.inv(mat),y)
    pars=np.dot(np.linalg.pinv(mat),y)
    p=pars[:n]
    q=pars[n:]
    return p,q


def lorentz(x):
    return 1/(1+x**2)

n=4
m=5
x=np.linspace(-1,1,n+m-1)
y=lorentz(x)
p,q=rat_fit(x,y,n,m)
xx=np.linspace(-1,1,1001)
y_true=lorentz(xx)
pred=rat_eval(p,q,xx)
plt.clf();plt.plot(x,y,'*',label="Data")
plt.plot(xx,y_true,label="True")
plt.plot(xx,pred,label="Interpolation")
#plt.ylim(-20,20)
plt.legend(loc='upper left')
plt.savefig('ratfit_lorentz.png')
print('my ratfit rms error is ',np.std(pred-y_true))
print(p,q)