import math as m
import numpy as np
import matplotlib.pyplot as plt
intrvl = 0.01
ho = float(input('Input initial height: '))
vo = float(input('Input initial velocity: '))
ang = float(input('Input angle of projectile: '))
ax = float(input('Input horizontal acceleration: '))
ay = float(input('Input vertical acceleration: '))

t = intrvl
ang = m.radians(ang)
vox = vo*m.cos(ang)
voy = vo*m.sin(ang)
rt = [ay/2, voy, ho]
tm = max(np.roots(rt))
d = np.arange(0,tm,intrvl)
x = np.zeros(len(d)+1)
y = np.zeros(len(d)+1)
x[0] = 0
y[0] = ho
n = np.arange(0,len(d)-1,1)
for i in n:
    xt = (ax*(t**2))/2 + vox*t
    yt = (ay*(t**2))/2 + voy*t + ho
    x[i+1] = xt
    y[i+1] = yt
    t=t+intrvl
x[len(d)] = (ax/2)*tm**2 + vox*tm
y[len(d)] = 0
if ay>=0:
    print ('ERROR! The vertical acceleration you entered was either positive or zero. Rerun the program.')
elif ay<0:        
    plt.plot(x,y)
    plt.title ('Distance vs Height')
    plt.xlabel('Distance')
    plt.ylabel('Height')
    
    
    
