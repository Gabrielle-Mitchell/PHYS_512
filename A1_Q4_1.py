import numpy as np
from matplotlib import pyplot as plt
import scipy.integrate

def fun(x,t):
    return (t - x)/((1 + t**2 - 2*t*x)**(1.5)) #integrand after angular substitution


def simple_integrate(fun,a,b,t,tol):
    
    fz=np.zeros(200)
    x=np.linspace(a,b,200)
    y=fun(x,t)
    dx=np.median(np.diff(x))
    fz=dx/3.0*(y[0]+y[-1]+4*np.sum(y[1::2])+2*np.sum(y[2:-1:2]))    #simpsons
    return fz

z = np.linspace(0.1,2.1,200)     #inside sphere to outside sphere
empty = np.empty(len(z))
for i in range(len(z)):
    empty[i]=simple_integrate(fun,-1,1,z[i],10e-5)

#print(empty)
plt.plot(z,empty,'.',label="My integrator")
plt.ylim(-3,3)

G= np.empty(len(z))             #use scipy built in integrator
for i in range(len(z)):
    f = lambda x : fun(x,z[i])
    G[i]=scipy.integrate.quad(f, -1, 1)[0]

plt.plot(z,G,'.',label="Scipy Integrator")
plt.ylim(-3,3)
plt.title('Electric Field from a Spherical Shell')
plt.xlabel('z')
plt.ylabel('Ez')
plt.legend(loc='upper left')
plt.savefig('Efield.png')