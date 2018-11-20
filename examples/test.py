#!/usr/bin/env python
import numpy as np

from GRAFS import GRAFS

grafs = GRAFS()

def schedule(t):
    if t<0.:
        ep1 = initialEp1
    elif t<epsStepTime:
        ep1 = initialEp1+(-initialEp1+entE1)*np.sin(t/epsStepTime*np.pi/2.)**2
    elif t<epsStepTime+waitTime:
        ep1 = entE1
    elif t< 2.*epsStepTime+waitTime:
        ep1 = entE1-(-initialEp1+entE1)*np.sin((t-(epsStepTime+waitTime))/epsStepTime*np.pi/2.)**2
    else:
        ep1 = initialEp1
    return ep1

epsStepTime = 5.
waitTime = 2.8
initialEp1=500.
entE1 = 90.

n = 101

times = np.linspace(0.,12.8,n)
eps = map(schedule,times)
eps = np.fromiter(eps, dtype=np.int)
