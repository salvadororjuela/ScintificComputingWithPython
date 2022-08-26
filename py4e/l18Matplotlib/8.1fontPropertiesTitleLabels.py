from matplotlib import pyplot as plt
import numpy as np

sistole = np.array([110, 120, 115, 100, 130])
diastole = np.array([70, 80, 75, 65, 90])

titleFont = {"family": "serif", "color": "red", "size": 15}
labelFont = {"family": "serif", "color": "green", "size": 10}

plt.plot(sistole, c = "r", lw = "2")
plt.plot(diastole, c = "g", lw = "2")

""" Position the Title
You can use the loc parameter in title() to position the title.
Legal values are: 'left', 'right', and 'center'. Default value is 'center'."""

plt.title("Last 5 Blood Pressure Samples", fontdict=titleFont, loc="left")
plt.xlabel("Blood pressure sample", fontdict=labelFont)
plt.ylabel("Diastole / Sistole", fontdict=labelFont)

plt.show()