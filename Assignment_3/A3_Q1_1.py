import numpy as np
from matplotlib import pyplot as plt
from scipy import interpolate
from mpl_toolkits import mplot3d 
data = np.loadtxt(".\Desktop\PHYS_512\Ass3\dish_zenith.txt") 

X=data[:,0]
Y=data[:,1]
Z=data[:,2]

def mat_A(x,y):
    A=np.zeros([475,4])
    A[:,0]=1
    A[:,1]=x**2+y**2
    A[:,2]=x
    A[:,3]=y
    return A

A=mat_A(X,Y)

#solve A^T N^-1 A m = A^T N-1 d with NO noise i.e. N=id
lhs=A.T@A
rhs=A.T@Z
m=np.linalg.inv(lhs)@rhs

#<d>=Am
z_pred=A@m
print('The parameter values are', m)

plt.clf()
ax = plt.axes(projection='3d')
ax.scatter3D(X, Y, Z, c=Z, cmap='Greens')   #plotting data
x=np.linspace(-3000,3000)
y=np.linspace(-3000,3000)
G, H = np.meshgrid(x, y)
def f(x, y, c0, c1, c2, c3):
    return c0 + c1*(x**2 + y**2) +c2*x + c3*y
JJ = f(G, H, m[0],m[1],m[2],m[3])     #this is the paraboloid for our model
ax.contour3D(G, H, JJ,100,cmap='binary')
plt.savefig('zenith_dish.png')

#what is the noise on the data points?
rms=np.std(Z-z_pred)
N=rms**2

Ninv=np.eye(len(Z))/N
lhs=A.T@Ninv@A
errs=np.sqrt(np.diag(np.linalg.inv(lhs)))
for i in range(len(m)):
    print('paramter ',i,' has value ',m[i],' and error ',errs[i])

#note that a=m[1]

f=0.25*(1/m[1])
un_f=(1/m[1]**2)*errs[1]    #using standard error propagation rules
print('The focal length is ',f,'with uncertainty ',un_f)