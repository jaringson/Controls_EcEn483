# Inverted ballbeam Parameter File
import numpy as np
# import control as cnt
import sys
sys.path.append('..')  # add parent directory
import ballbeamParam as P

# sample rate of the controller
Ts = P.Ts

# dirty derivative parameters
sigma = 0.05  # cutoff freq for dirty derivative
beta = (2 * sigma - Ts) / (2 * sigma + Ts)  # dirty derivative gain


# saturation limits
F_max = 15          		  # Max Force, N
theta_max = 5*np.pi/180.0  # Max theta, rads




kp_th  =  138 - 100
kd_th  =  10.2 + 45
ki_th = 0

kp_z   = -0.37 + .2
kd_z   = -0.27 - .25
ki_z = -0.01 

# kp_th= 77.9650
# ki_th= -0.0500
# kd_th= 7.6725
# kd_z= -0.2073
# ki_z= -0.0500
# kp_z= -0.2108

# print('DC_gain', DC_gain)
print('kp_th: ', kp_th)
print('kd_th: ', kd_th)
print('kp_z: ', kp_z)
print('ki_z: ', ki_z)
print('kd_z: ', kd_z)



