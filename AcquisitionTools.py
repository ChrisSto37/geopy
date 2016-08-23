# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 14:46:55 2016

@author: christian

ACQUISTION DESIGN TOOLS
"""

#import tkinter
import math

#PARAMETERS
GEO = 'orthogonal'
ILF = 6
XLF = 6

RD  =   25
SD  =   25
RLD =  250
SLD =  250

NRL =   20
NR =   120
SALVO = 10


#FUNCTIONS
def fold(ILF,XLF):
    return float(ILF*XLF)
    
def signalimprovement(fold):
    stn=math.sqrt(fold)
    return stn    
    
def XmaxIL(RD, NR):
    return (RD*NR)/2-(RD/2)

def XmaxXL(NRL, SALVO, RD, SD, RLD):
    return ((NRL-1)*RLD/2)+(SALVO/2*SD)-RD/2
        
def Xmax(XmaxIL, XmaxXL):
    return (math.sqrt(XmaxIL**2+XmaxXL**2))

def XminMax(RLD, SLD):
    return (math.sqrt(RLD**2+SLD**2))

def BinDen(RD, SD):
    return(1000000/(SD*RD))

def Effort(fold, BinDen):
    return(fold*BinDen)
    
#OUTPUT
fold=fold(ILF,XLF)
XmaxIL=XmaxIL(RD,NR)
XmaxXL=XmaxXL(NRL, SALVO, RD, SD, RLD)
Xmax=Xmax(XmaxIL, XmaxXL)
XminMax=XminMax(RLD, SLD)
BinDen=BinDen(RD, SD)
Effort=Effort(fold,BinDen)


print('Fold: ',fold)
print('S2N improvement:   ',signalimprovement(fold))
print('Maximum IL offset: ',XmaxIL)
print('Maximum XL offset: ',XmaxXL)
print('Max offset:         %6.2f' % (Xmax))
print('Max minimum offset: %6.2f' % (XminMax))
print('Bin density per km: %6.2f' % (BinDen))
print('Effort:             %6.2f' % (Effort))
