import matplotlib.pyplot as plt
import numpy as np

xpoints1 = np.array([3, 4, 6, 9])
ypoints1 = np.array([2, 8, 1, 10])
xpoints2 = np.array([2, 3, 5, 8])
ypoints2 = np.array([6, 2, 7, 11])

plt.plot(xpoints1, ypoints1, ls = "-.", c = "#00f", lw = "6")
plt.plot(xpoints2, ypoints2, ls = "-", c = "orange", lw = "5")
plt.show()
