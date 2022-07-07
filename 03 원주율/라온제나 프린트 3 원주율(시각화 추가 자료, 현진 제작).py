import numpy as np
import matplotlib.pyplot as plt
from matplotlib.artist import Artist
import random

theta = np.linspace(0, 2*np.pi, 100)

r = 1.0

x = r*np.cos(theta)
y = r*np.sin(theta)

fig, ax = plt.subplots(1)
ax.plot(x, y, color="black")
ax.vlines(-1, -1, 1, color="black")
ax.vlines(1, -1, 1, color="black")
ax.hlines(-1, -1, 1, color="black")
ax.hlines(1, -1, 1, color="black")

ax.set_aspect(1)
plt.xlim(-1.25, 1.25)
plt.ylim(-1.25, 1.25)
plt.grid(linestyle='--')

global text
text = ax.text(0.05, 0.95, '', transform=ax.transAxes, fontsize=10, verticalalignment='top')


def rand_dot(ax):
    a = random.uniform(-1, 1)
    b = random.uniform(-1, 1)
    mec = "red"
    mfc = "lightcoral"
    if a**2+b**2 < 1:
        mec = "blue"
        mfc = "lightblue"
        global inner
        inner += 1

    global total
    total += 1

    pi = inner / total * 4
    global text
    text.set_text(f'pi={pi}')
    ax.plot(a, b, marker="o", markersize=5, markeredgecolor=mec, markerfacecolor=mfc)
    fig.canvas.draw()


timer = fig.canvas.new_timer(interval=10)
timer.add_callback(rand_dot, ax)
timer.start()

global total
total = 0
global inner
inner = 0

plt.show()
