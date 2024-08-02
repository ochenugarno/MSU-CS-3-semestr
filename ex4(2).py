import numpy as np
import matplotlib.pyplot as plt
import math

step = 0.01
x1 = np.arange(-5, -4 + step, step)
x2 = np.arange(-4 + step, -3 + step, step)
x3 = np.arange(-3 + step, 2 + step, step)
x4 = np.arange(2 + step, 3 + step, step)
x5 = np.arange(3 + step, 5 + step, step)
y1 = np.sin(math.pi * x1)
y2 = -np.sin(math.pi * x2)
y3 = np.sin(math.pi * x3)
y4 = np.sin(3 * math.pi * x4)
y5 = np.sin(math.pi * x5)
X = np.hstack((x1, x2, x3, x4, x5))
Y = np.hstack((y1, y2, y3, y4, y5))
plt.plot(X, Y, color = 'red')
plt.show()