import numpy as np
import matplotlib.pyplot as plt

def riemann_left(y, x):
       area = 0
       for i in range(len(x) - 1): 
          area = area + y[i] * (x[i + 1] - x[i])
       return area # send back areaü
   
def riemann_center(y, x):
       area = 0
       for i in range(len(x) - 1): 
          area = area + (y[i]+y[i+1])/2 * (x[i + 1] - x[i])
       return area # send back area
  
def riemann_left_ciz(y, x):
    xyen=np.zeros((len(x)-1)*4)
    yyen=np.zeros((len(x)-1)*4)
    for i in range(len(x)-1):
        xyen[4*i]=x[i]
        xyen[4*i+1]=x[i]
        xyen[4*i+2]=x[i+1]
        xyen[4*i+3]=x[i+1]
        yyen[4*i]=0
        yyen[4*i+1]=y[i]
        yyen[4*i+2]=y[i]
        yyen[4*i+3]=0
    return xyen,yyen
def simpson13(y,x):
    # if len(x) % 2 == 1:
    #     print("Çift sayıda nokta olmalı")
    deltax = x[1] - x[0]
    alan = y[0] + y[-1]    
    for i in range(1,len(x)):
        if i%2 == 0:
            alan = alan + 2 * y[i]
        else:
            alan = alan + 4 * y[i]
    alan = alan * deltax/3
    return alan

def riemann_center_ciz(y, x):
    xyen=np.zeros((len(x)-1)*4)
    yyen=np.zeros((len(x)-1)*4)
    for i in range(len(x)-1):
        xyen[4*i]=x[i]
        xyen[4*i+1]=x[i]
        xyen[4*i+2]=x[i+1]
        xyen[4*i+3]=x[i+1]
        yyen[4*i]=0
        yyen[4*i+1]=np.cos((x[i + 1]+x[i])/2)
        yyen[4*i+2]=np.cos((x[i + 1]+x[i])/2)
        yyen[4*i+3]=0
    return xyen,yyen  

def trapez(y, x):
       area = 0 # starting value for area
       for i in range(len(x) - 1): 
          area = area + (y[i] + y[i + 1]) * (x[i + 1] - x[i]) / 2
       return area # send back area     
           
def trapez_ciz(y, x):
    xyen=np.zeros((len(x)-1)*4)
    yyen=np.zeros((len(x)-1)*4)
    for i in range(len(x)-1):
        xyen[4*i]=x[i]
        xyen[4*i+1]=x[i]
        xyen[4*i+2]=x[i+1]
        xyen[4*i+3]=x[i+1]
        yyen[4*i]=0
        yyen[4*i+1]=y[i]
        yyen[4*i+2]=y[i+1]
        yyen[4*i+3]=0
    return xyen,yyen   

def simps2(y,x):
    if (len(x)-1)% 2 == 1:
        print("Çift sayıda bölgeye")
    deltax= x[1] - x[0]
    alan = deltax/3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
    return alan

def simpson3(y,x):
    # calculating step size
    h = x[1] - x[0]
    
    # Finding sum 
    integration = y[0] + y[-1]
    
    for i in range(1,len(x)):
        # k = x0 + i*h
        
        if i%2 == 0:
            integration = integration + 2 * y[i]
            print("A")
        else:
            integration = integration + 4 * y[i]
            print("b")
    
    # Finding final integration value
    integration = integration * h/3
    
    return integration

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


xcizim=np.linspace(-np.pi/3,np.pi/2,100)
ycizim=np.cos(xcizim)
xyenl,yyenl=riemann_left_ciz(y, x)
plt.plot(xcizim,ycizim,xyenl,yyenl)
plt.scatter(x[:-1],y[:-1],color="red")
plt.figure()
xyenc,yyenc=riemann_center_ciz(y, x)
plt.plot(xcizim,ycizim,xyenc,yyenc)
scatx=list((x[i]+x[i+1])/2 for i in range(len(x)-1))
scaty=list(np.cos((x[i + 1]+x[i])/2) for i in range(len(x)-1))
plt.scatter(scatx,scaty,color="red")
 

plt.figure()                                       
xyen,yyen=trapez_ciz(y, x)

plt.plot(xcizim,ycizim,xyen,yyen)
plt.scatter(x,y,color="red")
from scipy.integrate import simps
