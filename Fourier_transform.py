# -*- coding: utf-8 -*-

from matplotlib import pyplot, rcParams, animation
from math import sin, cos, pi, e
import numpy as np

l_time = 4
bps = 3 #cycle
time = 0

rcParams['figure.figsize']=(6, 6)

#cycle = [0.01*i for i in range(0,100*l_time+1)]
time = [0.01*i for i in range(0, 101)]

fx = [e**(2*1j*pi*t) for t in time] #f(x)
#gt = [cos(b*pi*bps*2)+1 for b in cycle] #g(t)

#fg = [e**(2*1j*pi*t) * cos(b*pi*bps*2) for t, b in zip(time, cycle)]

fx = np.array(fx)
#gt = np.array(gt)
#fg = np.array(fg)

#pyplot.plot(cycle, gt)
#pyplot.show()

fig = pyplot.figure()
ax = pyplot.axes(xlim=(-4, 4), ylim=(-4, 4))
line, = ax.plot([], [], lw=2)

def init() :
    line.set_data([], [])
    return line,

def animate(i) :
    x = np.linspace(0, 2, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=20, blit=True)

pyplot.show()
#pyplot.plot(fg.real, fg.imag)
