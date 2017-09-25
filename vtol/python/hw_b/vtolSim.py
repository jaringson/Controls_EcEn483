import matplotlib.pyplot as plt
import sys
sys.path.append('..')  # add parent directory
import vtolParam as V
from signalGenerator import signalGenerator
from vtolAnimation import vtolAnimation
from plotData import plotData
from vtolDynamics import vtolDynamics

# instantiate ballbeam, controller, and reference classes
vtol = vtolDynamics()
reference = signalGenerator(amplitude=0.5, frequency=0.02)
forceR = signalGenerator(amplitude=1, frequency=1.5, y_offset = 3)
forceL = signalGenerator(amplitude=1, frequency=1, y_offset = 3)


# instantiate the simulation plots and animation
dataPlot = plotData()
animation = vtolAnimation()

t = V.t_start  # time starts at t_start
while t < V.t_end:  # main simulation loop
    # Get referenced inputs from signal generators
    ref_input = reference.square(t)
    # Propagate dynamics in between plot samples
    t_next_plot = t + V.t_plot
    while t < t_next_plot:  # updates control and dynamics at faster simulation rate
        fR = forceR.sin(t)
        fL = forceL.sin(t)
        f = [fR[0],fL[0]]
        vtol.propagateDynamics(f)  # Propagate the dynamics
        t = t + V.Ts  # advance time by Ts
    # update animation and data plots
    animation.drawVtol(vtol.states())
    dataPlot.updatePlots(t, ref_input, vtol.states(), f)
    plt.pause(0.0001)  # the pause causes the figure to be displayed during the simulation

# Keeps the program from closing until the user presses a button.
print('Press key to close')
plt.waitforbuttonpress()
plt.close()
