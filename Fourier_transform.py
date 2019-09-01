# -*- coding: utf-8 -*-

from matplotlib import rcParams
from matplotlib import pyplot as plt
from math import sin, cos, pi, e
import numpy as np

l_time = 4
bps = 3 #cycle
time = 0

rcParams['figure.figsize']=(6, 6)

cycle = [0.01*i for i in range(0,100*l_time+1)]
time = [0.005*i for i in range(0, 1001)]

gt = [cos(b*pi*bps*2) for b in cycle] #g(t)
fx = [e**(2*1j*pi*t) for t in time] #f(x)
fg = [e**(2*1j*pi*t) * (1 + cos(b*pi*bps*2)) for t, b in zip(time, cycle)]

fx = np.array(fx)
gt = np.array(gt)
fg = np.array(fg)

plt.plot(cycle, gt)
plt.show()
plt.plot(fx.real, fx.imag)
plt.plot(fg.real, fg.imag)
