# -*- coding: utf-8 -*-

from matplotlib import rcParams
from matplotlib import pyplot as plt
from math import cos, pi, e
import numpy as np

l_time = 1
fbps = 254 #cycle_1
sbps = 1432 #cycle_2
q = 0
x = []

rcParams['figure.figsize']=(6, 3)

cycle = [0.001*i for i in range(0,100*l_time+1)]
gt = [cos(b*pi*fbps*2) + cos(b*pi*sbps*2) for b in cycle] #g(t)
gt = np.array(gt)
plt.plot(cycle, gt)
plt.show()

#fx = [e**(2*1j*pi*t) for t in time] #f(x)

while(q < 0.2) :
    q += 0.0001
    time = [q*i for i in range(0, 10000)]
    cycle = [0.0001*i for i in range(0,100*l_time+1)]
    fg = [e**(2*1j*pi*t) * ((cos(b*pi*fbps*2) + cos(b*pi*sbps*2))) for t, b in zip(time, cycle)] #f(x)g(x)
    fg = np.array(fg)
    p1 = sum(fg.real) / len(fg)
    x.append(p1)

plt.plot(x, )
plt.show()
