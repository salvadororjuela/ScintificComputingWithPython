"""
Display Multiple Plots
With the subplot() function you can draw multiple plots in one figure.

The subplot() Function
The subplot() function takes three arguments that describes the layout of the figure.
The layout is organized in rows and columns, which are represented by the first and second argument.
The third argument represents the index of the current plot.

plt.subplot(1, 2, 1)
#the figure has 1 row, 2 columns, and this plot is the first plot.

plt.subplot(1, 2, 2)
#the figure has 1 row, 2 columns, and this plot is the second plot.

Title
You can add a title to each plot with the title() function.

Super Title
You can add a title to the entire figure with the suptitle() function
"""

from matplotlib import pyplot as plt
import numpy as np

labelText = {"family": "serif", "color": "red", "size": 8}
titleText = {"family": "serif", "color": "blue", "size": 12}
supertitle = {"family": "roman", "color": "orange", "size": 20}

# Plot 1
y1 = np.array([1, 3, 5])
plt.subplot(3, 2, 1)
plt.plot(y1, "D-g", lw=0.5)
plt.title("Lineal Increase", loc="left", fontdict=titleText) # Title and labels must be located after plt.plot
plt.xlabel("X Values", fontdict=labelText)
plt.ylabel("Y Values", fontdict=labelText)

# Plot 2
y2 = np.array([5, 3, 1])
plt.subplot(3, 2, 2)
plt.plot(y2, "D-g", lw=0.5)
plt.title("Lineal Decrease", loc="right", fontdict=titleText) # Title and labels must be located after plt.plot
plt.xlabel("X Values Decreasing", fontdict=labelText)
plt.ylabel("Y Values Decreasing", fontdict=labelText)

# Plot 3
x3 = np.array([10, 20, 30, 40, 50])
y3 = np.array([20, 15, 18, 12, 5])
plt.subplot(3, 2, 3)
plt.plot(x3, y3, marker = "o", markerfacecolor = "blue", markersize = 5, markeredgecolor = "r", lw = 0.5)
plt.title("Bear Tendency", loc = "right", fontdict=titleText)
plt.ylabel("Y Bear Tendency", fontdict=labelText)
plt.xlabel("X Bear Time", fontdict=labelText)

# Plot 4
x4 = np.array([10, 20, 30, 40, 50])
y4 = np.array([5, 12, 18, 15, 20])
plt.subplot(3, 2, 4)
plt.plot(x4, y4, "o--y", markerfacecolor = "yellow", markersize = 5, markeredgecolor = "b", lw = 0.5)
plt.title("Bull Tendency", loc = "right", fontdict=titleText) # Title and labels must be located after plt.plot
plt.ylabel("Y Bull Tendency", fontdict=labelText)
plt.xlabel("X Bull Time", fontdict=labelText)

# Plot 5
x5 = np.array([2, 4, 6, 8, 10, 12])
y5 = np.array([45, 50, 35, 40, 25, 30])
x6 = np.array([1, 3, 5, 7, 9, 11])
y6 = np.array([5, 50, 60, 15, 70, 75])
plt.subplot(3, 2, 6)
plt.plot(x5, y5, "v:y", markerfacecolor = "green", markersize = 5, markeredgecolor = "g", lw = 0.5)
plt.plot(x6, y6, "^-.g", markerfacecolor = "black", markersize = 5, markeredgecolor = "r", lw = 0.5)
plt.title("Both Tendencies in the Same Table", fontdict=titleText)
plt.xlabel("Year 2020", loc="right", fontdict=labelText)
plt.ylabel("Tendency Movements", fontdict=labelText)

# Create a Supertitle for the whole set
plt.suptitle("GRAPHICS COMPILATION",  )
# Display x and y grid
plt.grid(c="gray", ls="--", lw="0.5")
# plt.show() must be the final statement. If placed before, it will only display plots above it.
plt.show()