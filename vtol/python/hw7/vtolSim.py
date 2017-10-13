import sys
sys.path.append('..')  # add parent directory
import matplotlib.pyplot as plt
import numpy as np
import vtolParam as P
from vtolDynamics import vtolDynamics
from vtolController import vtolController
from signalGenerator import signalGenerator
from vtolAnimation import vtolAnimation
from plotData import plotData

# instantiate vtol, controller, and reference classes
vtol = vtolDynamics()
ctrl = vtolController()
reference = signalGenerator(amplitude=2, frequency=.01, y_offset = 3)

# instantiate the simulation plots and animation
dataPlot = plotData()
animation = vtolAnimation()

t = P.t_start  # time starts at t_start
while t < P.t_end:  # main simulation loop
    # Get referenced inputs from signal generators
    ref_input = reference.square(t)
    # Propagate dynamics in between plot samples
    t_next_plot = t + P.t_plot
    while t < t_next_plot: # updates control and dynamics at faster simulation rate
        u = ctrl.u(ref_input, vtol.outputs())  # Calculate the control value
        Fr = u[0]/2.0
        Fl = u[0]/2.0
        vtol.propagateDynamics([Fr, Fl])  # Propagate the dynamics
        t = t + P.Ts  # advance time by Ts
    # update animation and data plots
    animation.drawVtol(vtol.states())
    dataPlot.updatePlots(t, [[0],ref_input], vtol.states(), [Fr,Fl])
    plt.pause(0.0001)  # the pause causes the figure to be displayed during the simulation

# Keeps the program from closing until the user presses a button.
print('Press key to close')
plt.waitforbuttonpress()
plt.close()
