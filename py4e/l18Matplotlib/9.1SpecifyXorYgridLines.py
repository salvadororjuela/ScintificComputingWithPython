""" Specify Which Grid Lines to Display
You can use the axis parameter in the grid() function to specify which grid lines to display.
Legal values are: 'x', 'y', and 'both'. Default value is 'both'. """


import matplotlib.pyplot as plt
import numpy as np

sistole = np.array([110, 120, 115, 100, 130])
diastole = np.array([70, 80, 75, 65, 90])

titleFont = {"family": "serif", "color": "orange", "size": 20}
labelFont = {"family": "serif", "color": "red", "size": 15}

plt.title("Last 5 Blood Pressure Samples", loc="right", fontdict=titleFont)
plt.xlabel("Sample", loc="left", fontdict=labelFont)
plt.ylabel("Diastole / Sistole",  loc="center", fontdict=labelFont)

plt.plot(sistole, "D-y", lw = "1")
plt.plot(diastole, "o-.b", lw = "1.5")

plt.grid(axis="y", c="gray", ls="--", lw="0.5") # axis="x" to display the x grid
plt.show()
