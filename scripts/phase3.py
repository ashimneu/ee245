import numpy as np
from numpy import block
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d



tfinal = 60
numPoint = 200

t = np.linspace(0,tfinal, numPoint)


# 2d circular trajectory
omega0 = np.pi/30
theta = omega0*t

# 2d figure 8 trajectory
x = np.zeros(len(t))
y = np.zeros(len(t))



for j in range(len(t)):
    scale = 2.0/(3-np.cos(2*t[j]))
    x[j] = scale*np.cos(t[j])
    y[j] = scale*np.sin(2*t[j])/2
    # 

plt.plot(x,y,'g')


#plt.plot(t,z,'b')
#plt.plot(t,Y,'r')
#plt.plot(t,Phi,'w')
#plt.plot(t,Theta,'c')
#plt.plot(t,Psi,'y')
#plt.grid(linestyle='--', linewidth='0.5', color='white')

# Data for a three-dimensional line
#fig2 = plt.figure(2)
#ax = plt.axes(projection='3d')
#ax.plot3D(X, Y, Z, 'gray')
#plt.show()

