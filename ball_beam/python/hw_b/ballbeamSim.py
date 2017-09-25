import matplotlib.pyplot as plt
import sys
sys.path.append('..')  # add parent directory
import ballbeamParam as B
from signalGenerator import signalGenerator
from ballbeamAnimation import ballbeamAnimation
from plotData import plotData
from ballbeamDynamics import ballbeamDynamics

# instantiate ballbeam, controller, and reference classes
ballbeam = ballbeamDynamics()
reference = signalGenerator(amplitude=0.5, frequency=0.02)
force = signalGenerator(amplitude=1, frequency=.1, y_offset = 11)

# instantiate the simulation plots and animation
dataPlot = plotData()
animation = ballbeamAnimation()

t = B.t_start  # time starts at t_start
while t < B.t_end:  # main simulation loop
    # Get referenced inputs from signal generators
    ref_input = reference.square(t)
    # Propagate dynamics in between plot samples
    t_next_plot = t + B.t_plot
    while t < t_next_plot:  # updates control and dynamics at faster simulation rate
        f = force.sin(t)
        ballbeam.propagateDynamics(f)  # Propagate the dynamics
        t = t + B.Ts  # advance time by Ts
    # update animation and data plots
    # if ballbeam.states()[0] > B.l:
    #     print B.l
    #     print ballbeam.states()[0]
    #     ballbeam.states()[0] = B.l
    #     print "    ",ballbeam.states()[0]
    animation.drawBallbeam(ballbeam.states())
    dataPlot.updatePlots(t, ref_input, ballbeam.states(), f)
    plt.pause(0.0001)  # the pause causes the figure to be displayed during the simulation

# Keeps the program from closing until the user presses a button.
print('Press key to close')
plt.waitforbuttonpress()
plt.close()
