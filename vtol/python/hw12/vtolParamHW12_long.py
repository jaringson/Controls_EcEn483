# Single link arm Parameter File
import numpy as np
import control as cnt
import sys
sys.path.append('..')  # add parent directory
import vtolParam as P

Ts = P.Ts  # sample rate of the controller
beta = P.beta  # dirty derivative gain
F_max = P.F_max  # limit on control signal


####################################################
#                 State Space
####################################################
# tuning parameters
tr_h = .75       # rise time for position
zeta_h  = 0.707  # damping ratio angle
integrator_pole = -.275

# State Space Equations
# xdot = A*x + B*u
# y = C*x
A = np.matrix([[0.0, 1.0],
               [0.0, 0.0]])

B = np.matrix([[0.0],
               [1.0/(2*P.m+P.mc)]])

C = np.matrix([[1.0, 0.0]])

# form augmented system
A1 = np.matrix([[0.0, 1.0, 0.0],
               [0.0, 0.0, 0.0],
               [-1.0, 0.0, 0.0]])



B1 = np.matrix([[0.0],
               [1.0/(2*P.m+P.mc)],
               [0.0]])

# gain calculation
wn_h = 2.2/tr_h  # natural frequency for angle
des_char_poly = np.convolve(
	[1, 2*zeta_h*wn_h, wn_h**2], 
	np.poly(integrator_pole))
des_poles = np.roots(des_char_poly)

# Compute the gains if the system is controllable
if np.linalg.matrix_rank(cnt.ctrb(A1, B1)) != 3:
    print("The system is not controllable")
else:
    K1 = cnt.acker(A1, B1, des_poles)
    K = np.matrix([K1.item(0), K1.item(1)])
    ki = K1.item(2)

print('K: ', K)
print('ki: ', ki)

