import matplotlib.pyplot as plt
import numpy as np

sales = np.array([30, 10, 5, 5, 50])
products = np.array(["Chevrolet", "Mazda", "Toyota", "Peugeot", "Renault"])

# The startangle defines the angle of the initial wedge. This value is 0 by default
# and if defined is rotates counterclockwise
plt.pie(sales, labels = products, startangle = 90)
plt.show()