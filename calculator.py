import matplotlib
from mpl_toolkits.mplot3d import Axes3D
from Equation import Equation

import numpy as np
import matplotlib.pyplot as plt



fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

# set axis limits
x_min = y_min = z_min = -5
x_max = y_max = z_max = 5

ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)
ax.set_zlim(z_min, z_max)

e = Equation("4*x+x^2+4*x^3+y^2+y")
e.get_z_coords(x_min, x_max, y_min, y_max, z_min, z_max)

ax.plot(e.x_coords, e.y_coords, e.z_coords, 'black', alpha=0.2)



plt.show()