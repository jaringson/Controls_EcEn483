# Inverted ballbeam Parameter File
import numpy as np
import control as cnt
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

####################################################
#                 State Space
####################################################
# tuning parameters
tr_z = 0.25       # rise time for position
tr_theta = 0.50    # rise time for angle
zeta_z   = 0.707  # damping ratio position
zeta_th  = 0.707  # damping ratio angle
integrator_pole = -1  # integrator pole


# State Space Equations
# xdot = A*x + B*u
# y = C*x
A = np.matrix([[0.0, 0.0,               1.0,      0.0],
               [0.0, 0.0,               0.0,      1.0],
               [0.0, -P.g,          0.0,     0.0],
               [-3*P.m1*P.g/(P.m2*P.l**2), 0.0, 0.0, 0.0]])

B = np.matrix([[0.0],
               [0.0],
               [0.0],
               [3.0/(P.m2*P.l)]])

C = np.matrix([[1.0, 0.0, 0.0, 0.0],
               [0.0, 1.0, 0.0, 0.0]])


# form augmented system
A1 = np.matrix([[0.0, 0.0,               1.0,      0.0, 0.0],
               [0.0, 0.0,               0.0,      1.0, 0.0],
               [0.0, -P.g,          0.0,     0.0, 0.0],
               [-3*P.m1*P.g/(P.m2*P.l**2), 0.0, 0.0, 0.0, 0.0],
               [-1.0, 0.0, 0.0, 0.0, 0.0]])

B1 = np.matrix([[0.0],
               [0.0],
               [0.0],
               [3.0/(P.m2*P.l)],
               [0]])

# gain calculation
wn_th = 2.2/tr_theta  # natural frequency for angle
wn_z = 2.2/tr_z  # natural frequency for position
des_char_poly = np.convolve(
  np.convolve([1, 2*zeta_z*wn_z, wn_z**2], [1, 2*zeta_th*wn_th, wn_th**2]),
  np.poly(integrator_pole))
des_poles = np.roots(des_char_poly)

# Compute the gains if the system is controllable
if np.linalg.matrix_rank(cnt.ctrb(A1, B1)) != 5:
    print("The system is not controllable")
else:
    K1 = cnt.acker(A1, B1, des_poles)
    K = np.matrix([K1.item(0), K1.item(1), K1.item(2), K1.item(3)])
    ki = K1.item(4)
    # kr = -1.0/(C[0]*np.linalg.inv(A-B*K)*B)

print('K: ', K)
# print('kr: ', kr)
print('ki: ', ki)