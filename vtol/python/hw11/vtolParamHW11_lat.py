# Inverted ballbeam Parameter File
import numpy as np
import control as cnt
import sys
sys.path.append('..')  # add parent directory
import vtolParam as P

# sample rate of the controller
Ts = P.Ts

# dirty derivative parameters
sigma = 0.05  # cutoff freq for dirty derivative
beta = (2 * sigma - Ts) / (2 * sigma + Ts)  # dirty derivative gain


# saturation limits
tau_max = 1000             		  # Max Force, N

####################################################
#                 State Space
####################################################
# tuning parameters
tr_z = 2        # rise time for position
tr_theta = 0.8   # rise time for angle
zeta_z   = 0.707  # damping ratio position
zeta_th  = 0.707  # damping ratio angle

# State Space Equations
# xdot = A*x + B*u
# y = C*x
A = np.matrix([[0.0, 0.0,               1.0,      0.0],
               [0.0, 0.0,               0.0,      1.0],
               [0.0, -P.g,          -P.mu/(2*P.m+P.mc),     0.0],
               [0.0, 0.0, 0.0, 0.0]])

B = np.matrix([[0.0],
               [0.0],
               [0.0],
               [1.0/(2*P.m*P.d**2+P.Jc)]])

C = np.matrix([[1.0, 0.0, 0.0, 0.0],
               [0.0, 1.0, 0.0, 0.0]])

# gain calculation
wn_th = 2.2/tr_theta  # natural frequency for angle
wn_z = 2.2/tr_z  # natural frequency for position
des_char_poly = np.convolve([1, 2*zeta_z*wn_z, wn_z**2], [1, 2*zeta_th*wn_th, wn_th**2])
des_poles = np.roots(des_char_poly)

# Compute the gains if the system is controllable
if np.linalg.matrix_rank(cnt.ctrb(A, B)) != 4:
    print("The system is not controllable")
else:
    K = cnt.acker(A, B, des_poles)
    kr = -1.0/(C[0]*np.linalg.inv(A-B*K)*B)

print('K: ', K)
print('kr: ', kr)







