# Single link arm Parameter File
import numpy as np
# import control as cnt
import sys
sys.path.append('..')  # add parent directory
import vtolParam as P

Ts = P.Ts  # sample rate of the controller
beta = P.beta  # dirty derivative gain
F_max = P.F_max  # limit on control signal

# PD gains
#kp = 0.09 
#kd = 0.75 
tr = 2.0
wn = 2.2 / tr
zeta = .707
kp = 2*zeta*wn*(2*P.m+P.mc)
kd = wn**2*(2*P.m+P.mc)



print('kp: ', kp)
print('kd: ', kd)



