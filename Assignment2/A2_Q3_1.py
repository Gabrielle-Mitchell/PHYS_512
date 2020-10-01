import numpy as np
from scipy import integrate
from matplotlib import pyplot as plt

gab=np.array([1.41*1e20,2.08*1e8,2.41*1e6,7.74*1e12,2.38*1e12,5.04*1e10,3.3*1e9,1.86*1e4,16080,11940,1643*1e-6,7.03*1e9,1.58*1e11,1.2*1e10])

def fun(x,y,half_life=gab):
    #Have 15-state (14 decay reactions) radioactive decay
    dydx=np.zeros(len(half_life)+1)
    dydx[0]=-y[0]/half_life[0]
    for i in range(1,len(half_life)):
        dydx[i]=y[i-1]/half_life[i-1]-y[i]/half_life[i]   
    dydx[len(half_life)]=y[len(half_life)-1]/half_life[len(half_life)-1]
    return dydx

y0=np.asarray([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]) 
x0=1e12
x1=1e13
t_gab=np.linspace(x0,x1,101)
ans_stiff=integrate.solve_ivp(fun,[x0,x1],y0,method='Radau',t_eval=t_gab)
print(ans_stiff.y[0,-1],' with truth ',np.exp(-1*(x1-x0)))
#plt.plot(ans_stiff.t,ans_stiff.y[0,:])
#plt.title('U238')
#plt.savefig('U238.png')
#plt.clf()
#plt.plot(ans_stiff.t,ans_stiff.y[1,:])
#plt.title('Th234')
#plt.savefig('Th234.png')
#plt.clf()
#plt.plot(ans_stiff.t,ans_stiff.y[-1,:]/ans_stiff.y[0,:])
#plt.title('Pb206/U238')
#plt.savefig('Pb206_U238.png')
#plt.clf()
plt.plot(ans_stiff.t,ans_stiff.y[4,:]/ans_stiff.y[3,:])
plt.title('Th230/U234')
plt.savefig('Th230_U234.png')
