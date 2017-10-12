# Inverted Pendulum Parameter File
import numpy as np
import control as cnt

# Physical parameters of the inverted pendulum known to the controller
m = 5     # Mass of the cart, kg
ell = 0.5    # Length of the interest, m
g = 9.8       # Gravity, m/s**2
k = 3		# Spring Constant N/m 
b = 0.5      # Damping coefficient, Ns

# parameters for animation
w = 0.5       # Width of the cart, m
h = 0.15      # Height of the cart, m
gap = 0.005   # Gap between the cart and x-axis

# Initial Conditions
z0 = 0.0                # ,m
zdot0 = 0.0             # ,m/s

# Simulation Parameters
t_start = 0.0  # Start time of simulation
t_end = 100.0  # End time of simulation
Ts = 0.01  # sample time for simulation
t_plot = 1  # the plotting and animation is updated at this rate

# dirty derivative parameters
sigma = 0.05  # cutoff freq for dirty derivative
beta = (2.0*sigma-Ts)/(2.0*sigma+Ts)  # dirty derivative gain

# saturation limits
F_max = 2.0                # Max Force, N

