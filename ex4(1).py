import numpy as np
import matplotlib.pyplot as plt
import math


step = 0.01
t = np.arange(0, 5 + step, step)
x = t * np.cos(math.pi * t)
y = t * np.sin(math.pi * t)
plt.plot(x, y)
plt.show()