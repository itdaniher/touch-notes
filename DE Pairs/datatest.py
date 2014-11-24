#extremely rough data capture script, written from 1:00 to 2:15a / Mar3-2011
#code released under a beerware(http://en.wikipedia.org/wiki/Beerware)

#https://github.com/itdaniher/Python-SMU
import smu
#import pylab plotting functions
from pylab import plot, ion, xlabel, ylabel, title
#import numpy data-export function
from numpy import savetxt

smu = smu.smu()

from time import time

ion()

data = []
dataTime = [] 

smu.set_voltage(1, 2.25)
smu.set_voltage(2, 6)

print(smu.get_current(1), smu.get_current(2))
#20.63ma, .500ma

startTime = time()

while len(data) < 2000:
	dataTime.append(time() - startTime)
	data.append(smu.get_current(2))

plot(dataTime, data)
title("Response for PseudoLinear Manual Loading of D/E-based Touch Sensor")
xlabel("Time in Seconds")
ylabel("Milliamps through PhotoTransistor(6v bias)")

savetxt("data.txt", zip(dataTime, data))

