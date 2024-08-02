import numpy as np
from matplotlib.image import imread
import matplotlib.pyplot as plt


def bruhplot(values):
    wid = list(values).count(1)
    #np.sum(values==1, dtype='int')
    up = np.argmax(values)
    down = len(values) - np.argmax(values[::-1]) - 1
    SIU = (up <= 0.95 * len(values)) * ((up + wid//2) * ((down - up) > wid) + (up + down)//2 * ((down - up) <= wid))
    return SIU




img = imread('4.png')
Vbruhplot = np.vectorize(bruhplot, signature='(n)->()')

black_img = img[:, :, :1] .reshape(img.shape[:2])
black_img = (black_img < 0.5).astype(int)


xstr = np.sum(black_img, axis = 0)
ox = np.argmax(xstr)
ystr = np.sum(black_img, axis = 1)
oy = np.argmax(ystr)
black_spots = black_img[0: oy + 1, ox:]





Tblack_spots = black_spots.T[::]
Blen = len(black_spots[ox][::-1])
Bright = np.argmax(black_spots[oy][::-1])
Bdown = np.argmax(Tblack_spots[0])

Bxmass = np.arange(0, Blen - Bright, 1)
Bymass = (Vbruhplot(Tblack_spots[:Blen - Bright, Bdown:]))


red_img = img[:, :, 1:2].reshape(img.shape[:2])
red_img = (red_img < 0.4).astype(int)
red_spots = red_img[0: oy + 1, ox:]
red_spots -= black_spots
Tred_spots = red_spots.T[::]

Rxmass = np.arange(0, Blen - Bright, 1)
Rymass = (Vbruhplot(Tred_spots[:Blen - Bright, Bdown:]))

lmaoplot = np.vectorize(lambda lmao_x: (Bymass[lmao_x - 1] != 0) * lmao_x)

Bxmass = lmaoplot(Bxmass + 1)
Bxmass = Bxmass[Bxmass != 0] - 1
Bymass = Bymass[Bymass != 0]

siuplot = np.vectorize(lambda siu_x: (Rymass[siu_x - 1] != 0) * siu_x)

Rxmass = siuplot(Rxmass + 1)
Rxmass = Rxmass[Rxmass != 0] - 1
Rymass = Rymass[Rymass != 0]


fig, ax = plt.subplots()
ax.imshow(img)
ax.axis("off")
plt.plot(ox, oy, 'go')
plt.plot(ox + Rxmass[1:], Rymass[1:] + Bdown, 'r.', color = 'cyan', linewidth = 1)
plt.plot(ox + Bxmass[1:], Bymass[1:] + Bdown, 'r.', color = 'purple', linewidth = 1)
plt.show()
