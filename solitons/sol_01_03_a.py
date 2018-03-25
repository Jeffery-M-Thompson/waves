#!/usr/bin/env python3

# Get the libraries needed to animate the functions.

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

x = np.arange(-10, 10, 0.001)
line, = ax.plot(x, (2*np.exp(-x**2)+1))

def animate(i):
    line.set_ydata((2*np.exp(-(x+i/5.0)**2)+1))  # update the data
    return line,

# Init only required for blitting to give a clean slate.
def init():
    line.set_ydata(np.ma.array(x, mask=True))
    return line,

ani = animation.FuncAnimation(fig, animate, np.arange(1, 500), init_func=init,
interval=25, blit=True)
plt.show()