# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 00:00:24 2022

@author: Haktan Kaygısız
"""
import numpy as np

def riemann_left(y, x):
       alan = 0
       for i in range(len(x) - 1): 
          alan = alan + y[i] * (x[i + 1] - x[i])
       return alan

def riemann_center(y, x):
       alan = 0
       for i in range(len(x) - 1): 
          alan = alan + ((y[i]+y[i+1])/2) * (x[i + 1] - x[i])
       return alan
   
def trapez(y, x):
       alan = 0
       for i in range(len(x) - 1): 
          alan = alan + (y[i] + y[i + 1]) * (x[i + 1] - x[i]) / 2
       return alan

def simpson13(y,x):
    if (len(x)-1) % 2 == 1:
        print("Çift sayıda bölgeye ayrılmalı")
    deltax = x[1] - x[0]
    alan = y[0] + y[-1]    
    for i in range(1,len(x)):
        if i%2 == 0:
            alan = alan + 2 * y[i]
        else:
            alan = alan + 4 * y[i]
    alan = alan * deltax/3
    return alan


x=np.linspace(-np.pi/3,np.pi/2,11)
y=np.cos(x)
gercek=np.sin(np.pi/2)-np.sin(-np.pi/3)
print("Gerçek değeri \t:",round(gercek,3))
riemann_left=riemann_left(y, x)
print("Riemann sol \t:",round(riemann_left,3))
riemann_cent=riemann_center(y, x)
print("Riemann merkez \t:",round(riemann_cent,3))
trapz=trapez(y, x)
print("Trapez \t\t\t:",round(trapz,3))
simp=simpson13(y, x)
print("Simpson1/3\t\t:",round(simp,3))