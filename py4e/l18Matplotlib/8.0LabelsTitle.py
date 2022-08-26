import matplotlib.pyplot as plt
import numpy as np

pulse = np.array([50, 60, 70, 80, 90, 100, 110, 120, 130, 140])
burntCals = np.array([300, 350, 410, 470, 560, 650, 780, 910, 1050, 1300])

plt.plot(pulse, burntCals, ls = "-.", lw = "1")
plt.title("Calories vs Pulse / 1 hour")
plt.xlabel("Pulse")
plt.ylabel("Calories burnt in an hour")
plt.show()
