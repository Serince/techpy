# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 21:15:43 2022

@author: Haktan Kaygısız
"""
def forward(y, x):
       dyf = np.zeros(len(x))
       for i in range(len(x)-1):
            dyf[i] = (y[i + 1] - y[i]) / (x[i + 1] - x[i])
    
       dyf[-1]=(y[-1]-y[-2])/(x[-1]-x[-2])
    
       return dyf


     
       

def backward(y, x):
       dyb = np.zeros(len(x))
       for i in range(1,len(x)):
            dyb[i-1] = (y[i] - y[i - 1]) / (x[i] - x[i - 1])
       dyb[0]=(y[1]-y[0])/(x[1]-x[0])    
       return dyb
   
def central(y, x):
     dyc = np.zeros(len(x))
     for i in range(1,len(x)-1):
         dyc[i-1] = (y[i + 1] - y[i - 1]) / (x[i + 1] - x[i - 1])
         
     dyc[0]=(y[1]-y[0])/(x[1]-x[0])
     dyc[-1]=(y[-1]-y[-2])/(x[-1]-x[-2])

     return dyc
 
import matplotlib.pyplot as plt 
import numpy as np 
x = np.linspace(0, 2 * np.pi,20)
y = np.sin(x)
z = np.cos(x)
f = forward(y, x)
b = backward(y, x)
c = central(y, x)
plt.plot(x, z, x, f, x, b, x, c)
plt.legend(["cos(x)","İleri farklar", "Geri Farklar", "Merkezi Farklar"])