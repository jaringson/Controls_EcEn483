import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np 
import msdParam as S


class msdAnimation:
    '''
        Create pendulum animation
    '''
    def __init__(self):
        self.flagInit = True                  # Used to indicate initialization
        self.fig, self.ax = plt.subplots()    # Initializes a figure and axes object
        self.handle = []                      # Initializes a list object that will
                                              # be used to contain handles to the
                                              # patches and line objects.
        plt.axis([-3*S.ell,3*S.ell, -0.1, 3*S.ell]) # Change the x,y axis limits
        plt.plot([-2*S.ell,2*S.ell],[0,0],'b--')    # Draw a base line
        plt.xlabel('z')

        

        # Draw pendulum is the main function that will call the functions:
        # drawCart, drawCircle, and drawRod to create the animation.
    def drawMSD(self, u):
        # Process inputs to function
        z = u[0]        # Horizontal position of cart, m

        self.drawCart(z)
        self.drawBlock()

        self.ax.axis('equal') # This will cause the image to not distort

        # After each function has been called, initialization is over.
        if self.flagInit == True:
            self.flagInit = False

    def drawCart(self, z):
        x = z-S.w/2.0  # x coordinate
        y = S.gap      # y coordinate
        xy = (x, y)     # Bottom left corner of rectangle

        # When the class is initialized, a Rectangle patch object will be
        # created and added to the axes. After initialization, the Rectangle
        # patch object will only be updated.
        if self.flagInit == True:
            # Create the Rectangle patch and append its handle
            # to the handle list
            self.handle.append(mpatches.Rectangle(xy,
                S.w,S.h, fc = 'blue', ec = 'black'))
            self.ax.add_patch(self.handle[0]) # Add the patch to the axes
        else:
            self.handle[0].set_xy(xy)         # Update patch
    def drawBlock(self):
        if self.flagInit:
            self.handle.append(mpatches.Rectangle((-.80,0),
                    .05,1, fc = 'blue', ec = 'black'))
            self.ax.add_patch(self.handle[1]) # Add the patch to the axes
        else:
            self.ax.add_patch(self.handle[1])





# Used see the animation from the command line
if __name__ == "__main__":

    simAnimation = msdAnimation()    # Create Animate object
    z = 0.0                               # Position of cart, m
    theta = 0.0*np.pi/180                 # Angle of pendulum, rads
    simAnimation.drawMSD([z, theta, 0, 0])  # Draw the pendulum
    #plt.show()
    # Keeps the program from closing until the user presses a button.
    print('Press key to close')
    plt.waitforbuttonpress()
    plt.close()