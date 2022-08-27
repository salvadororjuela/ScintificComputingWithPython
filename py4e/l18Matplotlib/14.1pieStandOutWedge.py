""" To stand out a specific wedge, it is necessary to add another array
with the same number of elements of the previous ones. Each element is a 
number that indicate a distance from the rest of the pie and is asigned to the
explode= attribute """


import matplotlib.pyplot as plt
import numpy as np

sales = np.array([25, 25, 35, 15])
cars = np.array(["Chevrolet", "Nissan", "Renault", "Toyota"])
standOut = np.array([0, 0, 0.2, 0])
wedgeColors = np.array(["Aquamarine", "green", "yellow", "lime"])

# shadow= attribute to add a shadow to the pie. False is the default value.
plt.pie(sales, labels = cars, explode = standOut, shadow = True, colors = wedgeColors)
# Add a list of explanation for each wedge, and a title for the legend
plt.legend(title = "Car Brands")
plt.show()