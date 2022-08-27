from matplotlib import pyplot as plt
import numpy as np

months = np.array(["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC" ])
sales2021 = np.array([100, 110, 130, 120, 150, 100, 90, 80, 130, 140, 70, 200])
sales2022 = np.array([50, 60, 80, 90, 70, 150, 200, 130, 140, 210, 180, 300])

plt.subplot(1, 2, 1)
plt.title("Sales per Month 2021")
plt.xlabel("Months")
plt.ylabel("2021")
# Vertical bars with color and width properties
plt.bar(months, sales2021, color = "yellow", width = 0.5)

plt.subplot(1, 2, 2)
plt.title("Sales per Month 2022")
plt.xlabel("Months")
plt.ylabel("2022")
# Horizontal bars with color and height properties
plt.barh(months, sales2022, color = "green", height = 0.5)

plt.show()

""" width property is used in vertical bars, and height is used in horizontal bars."""