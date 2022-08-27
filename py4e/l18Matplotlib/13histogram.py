from matplotlib import pyplot as plt
import numpy as np

# The value assigned to the variable x correspond to 250 random values, with a
# standard deviatio of 10 around 170. This is Normal Data Distribution (AI)
x = np.random.normal(170, 10, 250)
plt.hist(x)
plt.show()