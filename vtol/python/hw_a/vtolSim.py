import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append('..')  # add parent directory
import vtolParam as V
from signalGenerator import signalGenerator
from vtolAnimation import vtolAnimation
from plotData import plotData


# instantiate reference input classes
reference = signalGenerator(amplitude=0.5, frequency=0.1)
zRef = signalGenerator(amplitude=0.9, frequency=0.7, y_offset=2.5) 
hRef = signalGenerator(amplitude=0.7, frequency=0.4, y_offset=2.5) 
ztRef = signalGenerator(amplitude=0.6, frequency=0.6, y_offset=2.5) 
thetaRef = signalGenerator(amplitude=np.pi/2, frequency=0.1)
fRef = signalGenerator(amplitude=5, frequency=.5)

print zRef

# instantiate the simulation plots and animation
dataPlot = plotData()
animation = vtolAnimation()

t = V.t_start  # time starts at t_start
while t < V.t_end:  # main simulation loop
    # set variables
    r = reference.square(t)
    z = zRef.sin(t)
    h = hRef.sin(t)
    zt = ztRef.sin(t)
    theta = thetaRef.sin(t)
    f = fRef.sawtooth(t)
    # update animation
    state = [z[0], h[0], theta[0], zt[0]]
    animation.drawVtol(state)
    dataPlot.updatePlots(t, r, state, f)

    t = t + V.t_plot  # advance time by t_plot
    plt.pause(0.1)

# Keeps the program from closing until the user presses a button.
print('Press key to close')
plt.waitforbuttonpress()
plt.close()