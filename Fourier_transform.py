# -*- coding: utf-8 -*-

from matplotlib import rcParams
from matplotlib import pyplot as plt
from math import cos, pi, e
import numpy as np
import heapq

l_time = 1
fbps = 254 #cycle_1
sbps = 1332 #cycle_2
q = 0
x = []
y = []

rcParams['figure.figsize']=(6, 3)

cycle = [0.01*i for i in range(0,100*l_time+1)]
gt = [cos(b*pi*fbps*2) + cos(b*pi*sbps*2) for b in cycle] #g(t)
gt = np.array(gt)
plt.plot(cycle, gt)
plt.show()

#fx = [e**(2*1j*pi*t) for t in time] #f(x)

while(q < 0.2) :
    q += 0.0001
    time = [q*i for i in range(0, 10000)]
    cycle = [0.0001*i for i in range(0,100*l_time+1)]
    fg = [e**(2*1j*pi*t) * ((0.3*cos(b*pi*fbps*2) + cos(b*pi*sbps*2))) for t, b in zip(time, cycle)] #f(x)g(x)
    fg = np.array(fg)
    p1 = sum(fg.real) / len(fg)
    x.append(p1)

for i in range(1, 2000) :
    if(x[i-1] < x[i] and x[i+1] < x[i]) :
        y.append(x[i]) #Maximum Value


plt.plot(x, )
plt.show()

res = heapq.nlargest(2, y)
print(x.index(res[0]))
print(x.index(res[1]))
