from matplotlib import pyplot as plt
import numpy as np

sistole = np.array([110, 120, 115, 100, 130])
diastole = np.array([70, 80, 75, 65, 90])

titleFont = {"family": "serif", "color": "blue", "size": 15}
labelFont = {"family": "serif", "color": "orange", "size": 8}

plt.plot(sistole, "D-r", lw = "1.5")
plt.plot(diastole, "D-b", lw = "1")

plt.ylabel("Diastole / Sistole", fontdict=labelFont)
plt.xlabel("Blood Pressure Sample", fontdict=labelFont)

plt.title("Last 5 Blood Pressure Samples", fontdict=titleFont, loc="right")

plt.grid() # Display all grid lines
plt.show()