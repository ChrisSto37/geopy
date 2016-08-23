# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 09:10:26 2016

@author: Christian Stotter

Calculates S/N as introduced by Liu and Li (1997)
"""

import obspy
from scipy import stats
from math import log
import matplotlib.pyplot as plt
import numpy as np

from obspy.io.segy.core import _read_segy
from obspy.core.util import get_example_file
# or 'from obspy import read' if file wide headers are of no interest
text='SSSA.sgy'
print(text)
filename = get_example_file(text)
st = _read_segy(filename)


#print (st)
#print(len (st))
#print(st.stats)

i=0
trace=np.zeros((1500, len(st)))
while i<len(st):
    trace[:, i]=st[i].data
    i=i+1



#plt.plot(trace[500,:])
plt.figure(figsize=(10,10))
plt.set_cmap('Greys')
plt.imshow(trace[1:800, :])

##spec=np.fft(trace)
#plt.figure(figsize=(10,10))
#spec=np.fft.fft2(trace)
#plt.imshow(abs(spec[1:250,1:100:])), plt.set_cmap('terrain')

#WINDOW DEFINITION
dt=0.004
xb=100
xe=200
tb=100
te=130
x=np.linspace(xb,xe,xe-xb+1)
x=np.int_(x)
t=np.linspace(tb,te,te-tb+1)
t=np.int_(t)
tracewin=trace[t,:]
tracewin=tracewin[:,x]
plt.imshow(tracewin)
tracewin=np.transpose(tracewin)


#SIGNAL TO NOISE RATIO
M=np.size(tracewin[:,1])
N=np.size(tracewin[1,:])
ES=0
EN=0

#ENERGY OF SIGNAL
for j in range (0, N):
    ESt=0    
    for i in range (0, M):
        ESt=ESt+tracewin[i, j]
        i+=1
    ES=ES+ESt**2
    print(ES)
    j+=1   
ES=ES/M
  
#ENERGY OF NOISE
for j in range (0, N):
    for i in range (0, M):
        EN=EN+tracewin[i, j]**2
        i+=1
    print(EN)
    j+=1  
    

EN=EN-ES

SNR=10*log(ES*M/(M*EN),10)

print("Signal to noise ratio= %5.2f or %5.2f in Dezibel" % (ES/EN, SNR))

