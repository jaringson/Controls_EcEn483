import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append('..')  # add parent directory
import ballbeamParam as B
from signalGenerator import signalGenerator
from ballbeamAnimation import ballbeamAnimation
from plotData import plotData


# instantiate reference input classes
reference = signalGenerator(amplitude=0.5, frequency=0.1)
zRef = signalGenerator(amplitude=0.5, frequency=0.7, y_offset=0.4) 
thetaRef = signalGenerator(amplitude=np.pi/2, frequency=0.1)
fRef = signalGenerator(amplitude=5, frequency=.5)

print zRef

# instantiate the simulation plots and animation
dataPlot = plotData()
animation = ballbeamAnimation()

t = B.t_start  # time starts at t_start
while t < B.t_end:  # main simulation loop
    # set variables
    r = reference.square(t)
    z = zRef.sin(t)
    theta = thetaRef.sin(t)
    f = fRef.sawtooth(t)
    # update animation
    state = [z[0], theta[0], 0.0, 0.0]
    animation.drawBallbeam(state)
    dataPlot.updatePlots(t, r, state, f)

    t = t + B.t_plot  # advance time by t_plot
    plt.pause(0.1)

# Keeps the program from closing until the user presses a button.
print('Press key to close')
plt.waitforbuttonpress()
plt.close()