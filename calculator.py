import matplotlib
from mpl_toolkits.mplot3d import Axes3D

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


# 4 = z^2 + x^2 + y^2

# # plot the z-axis
zline = np.linspace(-2, 2, 1000)

print (zline)

for i in zline:
    r = 4 - i*i
# xline = 
# yline = zline*zline

# ax.plot(xline,yline,zline)

# plt.show()