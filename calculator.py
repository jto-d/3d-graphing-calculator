import matplotlib
from mpl_toolkits.mplot3d import Axes3D
from Equation import Equation

import numpy as np
import matplotlib.pyplot as plt



fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

# set axis limits
x_min = -10
x_max = 10

y_min = -10
y_max = 10

z_min = -1
z_max = 1


ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)
ax.set_zlim(z_min, z_max)

# e = Equation("4*x+x^2+4*x^3+y^2+y")
# e.get_z_coords(x_min, x_max, y_min, y_max, z_min, z_max)

# ax.plot(e.x_coords, e.y_coords, e.z_coords, 'black', alpha=0.2)

x = np.linspace(x_min, x_max, 30)
y = np.linspace(y_min, y_max, 30)

X, Y = np.meshgrid(x,y)


print(eval("np.sin(np.sqrt(2 ** 2 + 2 ** 2))"))

def f(x,y):
    return(np.sin(np.sqrt(x ** 2 + y ** 2)))


Z = f(X,Y)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='binary')




plt.show()