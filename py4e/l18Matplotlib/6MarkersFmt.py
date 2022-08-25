import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([1, 3, 9, 5])

plt.plot(ypoints, "D-.c")
plt.show()

"""
The line value can be one of the following:

Line Reference
Line Syntax	Description
'-'	    Solid line	
':'	    Dotted line	
'--'	Dashed line	
'-.'	Dashed/dotted line
"""

"""
Color Reference
Color Syntax	Description
'r'	Red	
'g'	Green	
'b'	Blue	
'c'	Cyan	
'm'	Magenta	
'y'	Yellow	
'k'	Black	
'w'	White
"""