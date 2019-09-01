# -*- coding: utf-8 -*-

from matplotlib import pyplot, rcParams
from math import cos, pi, e
import numpy as np

l_time = 1
bps = 3

rcParams['figure.figsize']=(6, 3)

x = [0.01*i for i in range(0,100*l_time+1)]
a = [0.01*q for q in range(0, 100)]

fx = [e**(2*1j*pi*t) for t in a] #f(x)
gt = [cos(y*pi*bps*2)+1 for y in x] #g(t)

fx = np.array(fx)
gt = np.array(gt)

fxgt = [cos(y*pi*bps*2)*e**(2*1j*pi*t) for y, t in zip(x, a)]

fxgt = np.array(fxgt)

pyplot.plot(x, gt)
pyplot.show()
pyplot.plot(fx.real, fx.imag)
pyplot.show()
pyplot.plot(fxgt.real, fxgt.imag)
