import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x
    #return np.emath.sqrt(x)




def g(x):
    return x*x
    #return np.arctan(x)



def h(x):
    return np.exp(1j*(x+0j))
    #return np.sin(x)



values = np.loadtxt('C2.dat')
mass = values.T
x = mass[0]
y1 = mass[1]
y2 = mass[2]
f1 = f(x).real
f2 = f(x).imag
g1 = g(x).real
g2 = g(x).imag
h1 = h(x).real
h2 = h(x).imag
xs = []
ysR = []
ysI = []
M = [[sum(f1*f1)+sum(f2*f2), -sum(f1*f2)+sum(f2*f1), sum(f1*g1)+sum(f2*g2), -sum(f1*g2)+sum(f2*g1), sum(f1*h1)+sum(f2*h2), -sum(f1*h2)+sum(f2*h1)],
     [-sum(f2*f1)+sum(f1*f2), sum(f2*f2)+sum(f1*f1), -sum(f2*g1)+sum(f1*g2), sum(f2*g2)+sum(f1*g1), -sum(f2*h1)+sum(f1*h2), sum(f2*h2)+sum(f1*h1)],
     [sum(g1*f1)+sum(g2*f2), -sum(g1*f2)+sum(g2*f1), sum(g1*g1)+sum(g2*g2), -sum(g1*g2)+sum(g2*g1), sum(g1*h1)+sum(g2*h2), -sum(g1*h2)+sum(g2*h1)],
     [-sum(g2*f1)+sum(g1*f2), sum(g2*f2)+sum(g1*f1), -sum(g2*g1)+sum(g1*g2), sum(g2*g2)+sum(g1*g1), -sum(g2*h1)+sum(g1*h2), sum(g2*h2)+sum(g1*h1)],
     [sum(h1*f1)+sum(h2*f2), -sum(h1*f2)+sum(h2*f1), sum(h1*g1)+sum(h2*g2), -sum(h1*g2)+sum(h2*g1), sum(h1*h1)+sum(h2*h2), -sum(h1*h2)+sum(h2*h1)],
     [-sum(h2*f1)+sum(h1*f2), sum(h2*f2)+sum(h1*f1), -sum(h2*g1)+sum(h1*g2), sum(h2*g2)+sum(h1*g1), -sum(h2*h1)+sum(h1*h2), sum(h2*h2)+sum(h1*h1)]]

N = [[sum(f1*y1)+sum(f2*y2)], [-sum(f2*y1)+sum(f1*y2)], [sum(g1*y1)+sum(g2*y2)], [-sum(g2*y1)+sum(g1*y2)], [sum(h1*y1)+sum(h2*y2)], [-sum(h2*y1)+sum(h1*y2)]]

sol = np.linalg.solve(M, N).T
A = complex(sol[0][0], sol[0][1])
B = complex(sol[0][2], sol[0][3])
C = complex(sol[0][4], sol[0][5])
step = 0.01
X = np.arange(-4, 4 + step, step)
Yf = A * f(X) + B * g(X) + C * h(X)
Yreal = Yf.real
Yimag = Yf.imag
fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.set_xlabel('X')
ax1.set_ylabel('ReY')
ax2.set_xlabel('X')
ax2.set_ylabel('ImY')
ax1.plot(X, Yreal, color = 'red')
ax1.plot(x, y1, 'ro', color = 'red')
ax2.plot(X, Yimag, color = 'blue')
ax2.plot(x, y2, 'ro', color = 'blue')
plt.show()

