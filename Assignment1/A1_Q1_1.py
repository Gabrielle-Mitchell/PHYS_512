import numpy as np

expvals=np.linspace(-7,-1,13)
x0=1
#d(exp(x))/dx = exp(x)
#d**n(exp(0.01*x))/dx = (0.01**n)exp(0.01*x)
#truth=np.exp(x0)
truth=(np.exp(0.01*(x0)))*(0.01**5)
for myexp in expvals:
    dx=10**myexp
    #f1=np.exp(x0+dx)
    f1=np.exp(0.01*(x0+dx))
    #f2=np.exp(x0-dx) 
    f2=np.exp(0.01*(x0-dx))
    #f3=np.exp(x0+2*dx)
    f3=np.exp(0.01*(x0+2*dx))
    #f4=np.exp(x0-2*dx)
    f4=np.exp(0.01*(x0-2*dx))
    deriv=((2/3)*(f1-f2)/dx)-((1/12)*(f3-f4)/dx)  
    print(myexp,deriv,np.abs(deriv-truth))