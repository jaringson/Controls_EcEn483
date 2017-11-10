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
F_max = 150000          		  # Max Force, N
theta_max = 5*np.pi/180.0  # Max theta, rads




# kp_th  =  138 - 100
# kd_th  =  10.2 + 45
# ki_th = 0

# kp_z   = -0.37 + .2
# kd_z   = -0.27 - .25
# ki_z = -0.01 

# kp_th= 1.6133333333333335
# kd_th= 1.0369333333333335
# ki_th= 0.0
# kp_z= -0.03083588175331295
# kd_z= -0.07927624872579002  
# ki_z= -0.001

kp_th  =  -57.80952124 
kd_th  =  58.07220437
ki_th = 0

kp_z   = -24.55661081 
kd_z   = 6.2216 
ki_z = 0.0001 


# print('DC_gain', DC_gain)
print('kp_th: ', kp_th)
print('kd_th: ', kd_th)
print('kp_z: ', kp_z)
print('ki_z: ', ki_z)
print('kd_z: ', kd_z)



