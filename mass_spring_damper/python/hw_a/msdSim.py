import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append('..')  # add parent directory
import msdParam as S
from signalGenerator import signalGenerator
from msdAnimation import msdAnimation
from plotData import plotData


# instantiate reference input classes
reference = signalGenerator(amplitude=0.5, frequency=0.1)
zRef = signalGenerator(amplitude=0.5, frequency=0.3)
fRef = signalGenerator(amplitude=5, frequency=.5)

# instantiate the simulation plots and animation
dataPlot = plotData()
animation = msdAnimation()

t = S.t_start  # time starts at t_start
while t < S.t_end:  # main simulation loop
    # set variables
    r = reference.square(t)
    z = zRef.sin(t)
    f = fRef.sawtooth(t)
    # update animation
    state = [z[0], 0.0, 0.0]
    animation.drawMSD(state)
    dataPlot.updatePlots(t, r, state, f)

    t = t + S.t_plot  # advance time by t_plot
    plt.pause(0.1)

# Keeps the program from closing until the user presses a button.
print('Press key to close')
plt.waitforbuttonpress()
plt.close()