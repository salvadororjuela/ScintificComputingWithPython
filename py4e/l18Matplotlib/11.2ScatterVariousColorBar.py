import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# In addition you have to create an array with values (from 0 to 100), one value for each of the point in the scatter plot
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
# The argument s can change the size of each dot in the intersecion x, y.
# The array must have the same number of points
sizes = np.array([10, 40, 100, 30, 50, 70, 90, 150, 1000, 20, 80, 60, 600])

plt.scatter(x, y, c=colors, cmap = "viridis", s = sizes, alpha = 0.5) # the parameter alpha can also be passed in to get a transparency ie. alpha = 0.5
# Necessary to include the colormap into the drawing
plt.colorbar()
plt.show()

# An extensive list of ColorMaps is found in https://www.w3schools.com/python/matplotlib_scatter.asp