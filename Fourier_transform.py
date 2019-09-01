# -*- coding: utf-8 -*-

from matplotlib import rcParams
from matplotlib import pyplot as plt
from math import sin, cos, pi, e
import numpy as np

l_time = 10000
bps = 132 #cycle
q = 0
x = []
y = []

rcParams['figure.figsize']=(12, 6)

cycle = [0.0001*i for i in range(0,100*l_time+1)]

#gt = [cos(b*pi*bps*2) for b in cycle] #g(t)
#fx = [e**(2*1j*pi*t) for t in time] #f(x)

while(q < 0.1) :
    q += 0.0001
    time = [q*i for i in range(0, 100000)]
    fg = [e**(2*1j*pi*t) * (1 + cos(b*pi*bps*2)) for t, b in zip(time, cycle)] #f(x)g(x)
    fg = np.array(fg)
    p1 = sum(fg.real) / len(fg)
    p2 = sum(fg.imag) / len(fg)
    x.append(p1)
    y.append(p2)

#fx = np.array(fx)
#gt = np.array(gt)

#plt.plot(cycle, gt)
#plt.show()
#plt.plot(fx.real, fx.imag)
#plt.plot(fg.real, fg.imag)
plt.plot(x, )
