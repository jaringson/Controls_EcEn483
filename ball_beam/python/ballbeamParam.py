# Inverted Pendulum Parameter File
import numpy as np
import control as cnt

# Physical parameters of the inverted pendulum known to the controller
m1 = 0.35     # Mass of the ball, kg
m2 = 2.0      # Mass of the beam, kg
g = 9.8       # Gravity, m/s**2
l = 0.5  # Length of beam m

# parameters for animation
radius = 0.06 # Radius of circular part of pendulum

# Initial Conditions
z0 = 0.1                # ,m
theta0 = 0.6*np.pi/180  # ,rads
zdot0 = 0.0             # ,m/s
thetadot0 = 0.0         # ,rads/s

# Simulation Parameters
t_start = 0.0  # Start time of simulation
t_end = 50.0  # End time of simulation
Ts = 0.01  # sample time for simulation
t_plot = 0.1  # the plotting and animation is updated at this rate

# saturation limits
F_max = 100.0                # Max Force, N

