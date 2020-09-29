import numpy as np
from matplotlib import pyplot as plt

def cheb_fit(fun,ord):
    x=np.linspace(-1,1,ord+1)
    xx=0.25*x + 0.75    #Linear shift to new domain
    y=fun(xx)   
    mat=np.zeros([ord+1,ord+1])
    mat[:,0]=1
    mat[:,1]=x     
    for i in range(1,ord):
        mat[:,i+1]=2*x*mat[:,i]-mat[:,i-1]     
    coeffs=np.linalg.inv(mat)@y
    return mat,coeffs,xx
    
fun=np.log2
ord=20
x=np.linspace(0.5,1,ord+1)
trunc=7 #truncated (trunc-1)th order polynomial
mat,coeffs,xx=cheb_fit(fun,ord)
y=fun(x)
cheb=np.dot(mat[:,:trunc],coeffs[:trunc])
#print(coeffs,xx,coeffs[:trunc])

Lcoeffs=np.polynomial.legendre.legfit(x,y,6)    #numpy Legendre fit: 6th order
Lpoly=np.polynomial.legendre.legval(x,Lcoeffs)

plt.clf();
plt.plot(x,y,label="True")
plt.plot(xx,cheb,'*',label="Chebyshev Interpolation")
plt.plot(x,Lpoly,'.',label="Legendre Fit")
plt.legend(loc='upper left')
plt.savefig('cheby_log_interp.png')
plt.show()
plt.clf();
plt.plot(xx,cheb-y,label="Chebyshev Residual")
plt.plot(x,Lpoly-y,label="Legendre Residual")
plt.legend(loc='upper left')
plt.savefig('cheby_leg_resid.png')
plt.show()

print('rms error for chebyshev interpolation is ',np.sqrt(np.mean((cheb-y)**2)),' with max error ',np.max(np.abs(cheb-y)))
print('rms error for Legendre polyfit is ',np.sqrt(np.mean((Lpoly-y)**2)),' with max error ',np.max(np.abs(Lpoly-y)))