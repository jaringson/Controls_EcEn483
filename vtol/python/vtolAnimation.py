import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np 
import vtolParam as V


class vtolAnimation:
    '''
        Create pendulum animation
    '''
    def __init__(self):
        self.flagInit = True                  # Used to indicate initialization
        self.fig, self.ax = plt.subplots()    # Initializes a figure and axes object
        self.handle = []                      # Initializes a list object that will
                                              # be used to contain handles to the
                                              # patches and line objects.

        plt.axis([-2*V.length,2*V.length, -0.1, 2*V.length]) # Change the x,y axis limits
        plt.plot([0,5],[0,0],'b--')    # Draw a base line
        plt.plot([0,0],[0,5],'b--')    # Draw a base line
        plt.xlabel('z(m)')
        plt.ylabel('h(m)')

        

        # Draw pendulum is the main function that will call the functions:
        # drawCart, drawCircle, and drawRod to create the animation.
    def drawVtol(self, u):
        # Process inputs to function
        z = u[0]        # Horizontal position of cart, m
        h = u[1]
        theta = u[2]   # Angle of pendulum, rads
        zt = u[6]


        self.drawBody(z,h,theta)
        self.drawRR(z,h,theta)
        self.drawLR(z,h,theta)
        self.drawTarget(zt)

        self.ax.axis('equal') # This will cause the image to not distort

        # After each function has been called, initialization is over.
        if self.flagInit == True:
            self.flagInit = False

    def drawBody(self, z, h, theta):
        
        # points that define the base
        pts =np.matrix([
            [-V.width/2.0, -V.length/2.0],
            [+V.width/2.0, -V.length/2.0],
            [+V.width/2.0, +V.length/2.0],
            [-V.width/2.0, +V.length/2.0]]).T
        
        R = np.matrix([[np.cos(theta), -np.sin(theta)],
                       [np.sin(theta), np.cos(theta)]])
        T = np.matrix([z,h]).T
        pts = R*pts + T
        xy = np.array(pts.T)

        # When the class is initialized, a polygon patch object will be
        # created and added to the axes. After initialization, the polygon
        # patch object will only be updated.
        if self.flagInit == True:
            # Create the Rectangle patch and append its handle
            # to the handle list
            self.handle.append(mpatches.Polygon(xy, facecolor='blue', edgecolor='black'))
            self.ax.add_patch(self.handle[0]) # Add the patch to the axes
        else:
            self.handle[0].set_xy(xy)         # Update polygon

    def drawRR(self,z,h,theta):
        x = z + (V.width + V.radius)*np.cos(theta)        # x coordinate
        y = h + (V.length + V.radius)*np.sin(theta)       # y coordinate
        xy = (x,y)                                   # Center of circle

        # When the class is initialized, a CirclePolygon patch object will
        # be created and added to the axes. After initialization, the
        # CirclePolygon patch object will only be updated.
        if self.flagInit == True:
            # Create the CirclePolygon patch and append its handle
            # to the handle list
            self.handle.append(mpatches.CirclePolygon(xy,
                radius = V.radius, resolution = 15,
                fc = 'limegreen', ec = 'black'))
            self.ax.add_patch(self.handle[1])  # Add the patch to the axes
        else:
            self.handle[1]._xy=xy

    def drawLR(self,z,h,theta):
        x = z - (V.width + V.radius)*np.cos(theta)        # x coordinate
        y = h - (V.length + V.radius)*np.sin(theta)       # y coordinate
        xy = (x,y)                                   # Center of circle

        # When the class is initialized, a CirclePolygon patch object will
        # be created and added to the axes. After initialization, the
        # CirclePolygon patch object will only be updated.
        if self.flagInit == True:
            # Create the CirclePolygon patch and append its handle
            # to the handle list
            self.handle.append(mpatches.CirclePolygon(xy,
                radius = V.radius, resolution = 15,
                fc = 'limegreen', ec = 'black'))
            self.ax.add_patch(self.handle[2])  # Add the patch to the axes
        else:
            self.handle[2]._xy=xy

    def drawTarget(self,zt):


        x = zt  # x coordinate
        y = V.gap      # y coordinate
        xy = (x, y)     # Bottom left corner of rectangle

        # When the class is initialized, a Rectangle patch object will be
        # created and added to the axes. After initialization, the Rectangle
        # patch object will only be updated.
        if self.flagInit == True:
            # Create the Rectangle patch and append its handle
            # to the handle list
            self.handle.append(mpatches.Rectangle(xy,
                V.w,V.h, fc = 'blue', ec = 'black'))
            self.ax.add_patch(self.handle[3]) # Add the patch to the axes
        else:
            self.handle[3].set_xy(xy)         # Update patch





# Used see the animation from the command line
if __name__ == "__main__":

    simAnimation = ballbeamAnimation()    # Create Animate object
    z = 0.0                               # Position of cart, m
    theta = 0.0*np.pi/180                 # Angle of pendulum, rads
    simAnimation.drawVtol([z, theta, 0, 0])  # Draw the pendulum
    #plt.show()
    # Keeps the program from closing until the user presses a button.
    print('Press key to close')
    plt.waitforbuttonpress()
    plt.close()