# Inverted ballbeam Parameter File
import numpy as np
# import control as cnt
import sys
sys.path.append('..')  # add parent directory
import vtolParam as P

# sample rate of the controller
Ts = P.Ts

# dirty derivative parameters
sigma = 0.05  # cutoff freq for dirty derivative
beta = (2 * sigma - Ts) / (2 * sigma + Ts)  # dirty derivative gain

####################################################
#       PD Control: Time Design Strategy
####################################################
# tuning parameters
tr_th = 0.8          # Rise time for inner loop (theta)
zeta_th = 0.707       # Damping Coefficient for inner loop (theta)
M = 10.0              # Time scale separation between inner and outer loop
zeta_z = 0.707        # Damping Coefficient fop outer loop (z)
ki_z = -0.001

# saturation limits
tau_max = 1000             		  # Max Force, N
error_max = 100        		  # Max step size,m
theta_max = 180*np.pi/180.0  # Max theta, rads




kp_th = 0.372075 +1.5
kd_th = 0.1913142 -.15
kp_z = -0.007716836734693878 - .004
kd_z = -0.032875850340136056 - .005

print('DC_gain', DC_gain)
print('kp_th: ', kp_th)
print('kd_th: ', kd_th)
print('kp_z: ', kp_z)
print('ki_z: ', ki_z)
print('kd_z: ', kd_z)






