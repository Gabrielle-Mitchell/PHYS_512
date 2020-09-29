import numpy as np

def fun(x):
    return np.exp(x)

def lorentz(x):
    return 1/(1+x**2)

def simpson_rule(fun,a,b,y):
    f1=(y[0]+4*y[2]+y[4])/6.0*(b-a)
    f2=(y[0]+4*y[1]+2*y[2]+4*y[3]+y[4])/12.0*(b-a)  #simpson's rule
    xm=0.5*(a+b)
    return (xm,f1,f2)

def yL_value(fun,a,b,y):
    x=np.linspace(a,b,5)
    #print(x)
    return np.array([y[0], fun(x[1]), y[1], fun(x[3]), y[2]])   #left side recursion pattern (only two new function evaluations)

def yR_value(fun,a,b,y):
    x=np.linspace(a,b,5)
    #print(x)
    return np.array([y[2], fun(x[1]), y[3], fun(x[3]), y[4]])   #right side recursion pattern (only two new function evaluations)

def rec_int(fun,a,b,y,tol):
    (xm,f1,f2)=simpson_rule(fun,a,b,y)
    if (np.abs(f1-f2)<tol):
        return (16.0*f2-f1)/15.0    
    else:
        fL=rec_int(fun,a,xm,yL_value(fun,a,xm,y),tol/2)     #varying step size
        fR=rec_int(fun,xm,b,yR_value(fun,xm,b,y),tol/2)
        f=fL+fR
        return f   

def final_int(fun,a,b,tol):
    xab=np.linspace(a,b,5)
    yab=fun(xab)
    return rec_int(fun,a,b,yab,tol)

print('Exponential integral', final_int(fun,-1,1,1e-3))
print('Lorentzian integral', final_int(lorentz,-1,1,1e-3))