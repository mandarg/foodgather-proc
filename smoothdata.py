#! /usr/bin/env python

from pylab import plot,xlabel,ylabel,show,imshow,ylim,xlim
from numpy import arange,array,loadtxt,empty, append, mean
from math import sin,cos,pi
from numpy.fft import rfft,irfft
from copy import copy
import csv


load = open("kitchenmeallog.csv","rU")
array = []


for line in load.readlines()[1:]:
    splt = line.split(',')
    if splt[2] == "lunch" or splt[2] == "Lunch":
        add = splt[4]
        try:
            out = float(splt[4])
        except:
            out = float(0)
        array.append(out)

c = rfft(array)
abso = abs(c)**2
c_10 = copy(c)
c_2 = copy(c)

maxc = len(c)
max10 = (maxc//10)
max2 = (maxc//100)*2

for i in range(0, maxc):
    if max10 < i:
        c_10[i]=0
    if max2 < i:
        c_2[i]=0

new10 = irfft(c_10)
new2 = irfft(c_2)
new2 = append(new2, mean(new2))
newc = irfft(c)

# write smoothed data
myfile = open('smoothedlunchdata.csv', 'wb')
wr = csv.writer(myfile)
wr.writerow(new2)

#plot(new10)
plot(new2)

#plot(newc)
show()

