# Inverted Pendulum Parameter File
import numpy as np
import control as cnt

# Physical parameters of the inverted pendulum known to the controller
mr = 0.25     # Mass of the right prop, kg
ml = 0.25      # Mass of the left prop, kg
m = 0.25 		# Mass if left and right prop equal, kg
g = 9.8       # Gravity, m/s**2
mu = 0.1      # Viscous drag, kg/s
length = .2	
width = .2
Jc = .0042 	# Inertia kg m**2
d = 0.3      # Distance from vtol body to props, m
mc = 1 		# mass of the vtol body, kg

# parameters for animation
w = 0.15       # Width of the cart, m
h = 0.15      # Height of the cart, m
gap = 0.005   # Gap between the cart and x-axis
radius = 0.06 # Radius of circular part of pendulum

# Initial Conditions
z0 = 0.0                # ,m
h0 = 2.0				# ,m
theta0 = 0.0*np.pi/180  # ,rads
zdot0 = 0.0             # ,m/s
hdot0 = 0.0				# ,m/s
thetadot0 = 0.0         # ,rads/s
zt0 = 0.0				# ,m

# Simulation Parameters
t_start = 0.0  # Start time of simulation
t_end = 50.0  # End time of simulation
Ts = 0.01  # sample time for simulation
t_plot = 0.1  # the plotting and animation is updated at this rate

# dirty derivative parameters
sigma = 0.05  # cutoff freq for dirty derivative
beta = (2.0*sigma-Ts)/(2.0*sigma+Ts)  # dirty derivative gain

# saturation limits
F_max = 10.0                # Max Force, N

