from random import randint
import math
import matplotlib.pyplot as plt


def rayleigh_theory(x, sigma):
    return x/sigma**2 * math.exp(-x**2/2/sigma**2)


def rayleigh(sigma):
    ksi = randint(0, 99999)/100000
    r_ans = sigma * math.sqrt(math.log(1/(1 - ksi) ** 2))
    return r_ans


def THE_ULTIMATE_SUPER_STATISTICS(sigma):
    dr = 0.01
    bruh_statistics = dict()
    spot_num = 1000000
    for lmao in range(spot_num):
        root = rayleigh(sigma)
        edge1 = int(root / dr)
        edge2 = int(root / dr) + 1
        if root/dr - edge1 <= edge2 - root/dr:
            bruh_statistics[edge1 * dr] = bruh_statistics.get(edge1 * dr, 0) + 1/spot_num
        else:
            bruh_statistics[edge2 * dr] = bruh_statistics.get(edge2 * dr, 0) + 1/spot_num
    return bruh_statistics


fig, (ax1, ax2) = plt.subplots(2, 1)
sigma = 3
a = THE_ULTIMATE_SUPER_STATISTICS(sigma)
ax2.scatter(a.keys(), a.values())
x = [i/100 for i in range(0, 501)]
y = [rayleigh_theory(i, sigma) for i in x]
ax1.plot(x, y, color = 'blue')


sr = 0
for key, value in a.items():
    sr += key * value
print('СРЕДНЕЕ ЗНАЧЕНИЕ:', 'ТЕОРИЯ -', (math.pi/2)**0.5 * sigma, ',', 'ЭКСПЕРИМЕНТ -', sr)


dis = 0
for key, value in a.items():
    dis += value * (sr - key)**2
print('ДИСПЕРСИЯ:', 'ТЕОРИЯ -', (2 - math.pi/2) * sigma**2, ',', 'ЭКСПЕРИМЕНТ -', dis)
plt.show()




