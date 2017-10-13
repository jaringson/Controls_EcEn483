import sys
sys.path.append('..')  # add parent directory
import matplotlib.pyplot as plt
import numpy as np
import vtolParam as P
from vtolDynamics import vtolDynamics
from vtolController_lat import vtolController_lat
from vtolController_long import vtolController_long
from signalGenerator import signalGenerator
from vtolAnimation import vtolAnimation
from plotData import plotData


def saturate_F(u, limit):
    if abs(u) > limit:
        u = limit*np.sign(u)
    return u

# instantiate vtol, controller, and reference classes
vtol = vtolDynamics()
ctrl_lat = vtolController_lat()
ctrl_long = vtolController_long()
reference_h = signalGenerator(amplitude=0.01, frequency=.01, y_offset = 3)
reference_z = signalGenerator(amplitude=2.5, frequency=.08, y_offset = 3.0)

# instantiate the simulation plots and animation
dataPlot = plotData()
animation = vtolAnimation()

t = P.t_start  # time starts at t_start
while t < P.t_end:  # main simulation loop
    # Get referenced inputs from signal generators
    ref_input_z = reference_z.square(t)
    ref_input_h = reference_h.square(t)
    # Propagate dynamics in between plot samples
    t_next_plot = t + P.t_plot
    while t < t_next_plot: # updates control and dynamics at faster simulation rate
        u_tau = ctrl_lat.u(ref_input_z, vtol.states())  # Calculate the control value
        u_F = ctrl_long.u(ref_input_h, vtol.states())  # Calculate the control value
        #u_F = [(2*P.m+P.mc)*P.g] 
        Fr = (u_F[0]/2.0) + ((1.0 / (2*P.d)) * u_tau[0]) 
        Fl = (u_F[0]/2.0) - ((1.0 / (2*P.d)) * u_tau[0]) 
        Fr = saturate_F(Fr, 10)
        Fl = saturate_F(Fl, 10)
        vtol.propagateDynamics([Fr,Fl])  # Propagate the dynamics
        t = t + P.Ts  # advance time by Ts
    # update animation and data plots
    animation.drawVtol(vtol.states())
    dataPlot.updatePlots(t, [ref_input_z,ref_input_h] , vtol.states(), [Fr,Fl])
    plt.pause(0.0001)  # the pause causes the figure to be displayed during the simulation

# Keeps the program from closing until the user presses a button.
print('Press key to close')
plt.waitforbuttonpress()
plt.close()
