from matplotlib import pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, ls = ":", color = "r", linewidth = "15.5")
plt.show()

plt.plot(ypoints, ls = "--", c = "#00FF00", lw = "12")
plt.show()

"""
 Style	            Or
'solid' (default)	'-'	
'dotted'	        ':'	
'dashed'	        '--'	
'dashdot'	        '-.'	
'None'	            '' or ' '
"""