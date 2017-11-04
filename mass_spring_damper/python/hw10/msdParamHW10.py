# Single link arm Parameter File
import numpy as np
# import control as cnt
import sys
sys.path.append('..')  # add parent directory
import msdParam as P

Ts = P.Ts  # sample rate of the controller
beta = P.beta  # dirty derivative gain
F_max = P.F_max  # limit on control signal

# PD gains
#kp = 4.5
#kd = 12
#kp = 3.05
#kd = 7.2
tr = 2.6
zeda = 0.7
kp = (2.2/tr)**2 * P.m - P.k
kd = 2*0.7*(2.2/tr)*P.m-P.b
ki = 0.08


kp = 0.5798816568047336 + .5
kd = 5.423076923076923 -2#+ 1


print('kp: ', kp)
print('ki: ', ki)
print('kd: ', kd)



