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

# # plot the z-axis
# zline = np.linspace(z_min*2, z_max*2, 1000)
# xline = np.full((1,1000),0)[0]
# yline = np.full((1,1000),0)[0]
# ax.plot(xline, yline, zline, 'black')

# # plot the y-axis
# zline = np.full((1,1000),0)[0]
# xline = np.full((1,1000),0)[0]
# yline = np.linspace(y_min*2, y_max*2, 1000)
# ax.plot(xline, yline, zline, 'black')

# # plot the x-axis
# zline = np.full((1,1000),0)[0]
# xline = np.linspace(x_min*2, x_max*2, 1000)
# yline = np.full((1,1000),0)[0]
# ax.plot(xline, yline, zline, 'black')


plt.show()