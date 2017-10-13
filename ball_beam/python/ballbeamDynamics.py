import numpy as np 
import random
import ballbeamParam as B


class ballbeamDynamics:
    '''
        Model the physical system
    '''

    def __init__(self):
        # Initial state conditions
        self.state = np.matrix([[B.z0],          # z initial position
                                [B.theta0],      # Theta initial orientation
                                [B.zdot0],       # zdot initial velocity
                                [B.thetadot0]])  # Thetadot initial velocity
        #################################################
        # The parameters for any physical system are never known exactly.  Feedback
        # systems need to be designed to be robust to this uncertainty.  In the simulation
        # we model uncertainty by changing the physical parameters by a uniform random variable
        # that represents alpha*100 % of the parameter, i.e., alpha = 0.2, means that the parameter
        # may change by up to 20%.  A different parameter value is chosen every time the simulation
        # is run.
        alpha = 0.2  # Uncertainty parameter
        self.m1 = B.m1 #* (1+2*alpha*np.random.rand()-alpha)  # Mass of the pendulum, kg
        self.m2 = B.m2 #* (1+2*alpha*np.random.rand()-alpha)  # Mass of the cart, kg
        self.l = B.l #* (1+2*alpha*np.random.rand()-alpha)  # Length of the rod, m
        self.g = B.g  # the gravity constant is well known and so we don't change it.

    def propagateDynamics(self, u):
        '''
            Integrate the differential equations defining dynamics
            B.Ts is the time step between function calls.
            u contains the system input(s).
        '''
        # Integrate ODE using Runge-Kutta RK4 algorithm
        k1 = self.derivatives(self.state, u)
        k2 = self.derivatives(self.state + B.Ts/2*k1, u)
        k3 = self.derivatives(self.state + B.Ts/2*k2, u)
        k4 = self.derivatives(self.state + B.Ts*k3, u)
        self.state += B.Ts/6 * (k1 + 2*k2 + 2*k3 + k4)
        if self.state[0] > B.l:
            self.state[0] =  B.l

    def derivatives(self, state, u):
        '''
            Return xdot = f(x,u), the derivatives of the continuous states, as a matrix
        '''
        # re-label states and inputs for readability
        z = state.item(0)
        theta = state.item(1)
        zdot = state.item(2)
        thetadot = state.item(3)
        F = u[0]
        # The equations of motion.

        M = np.matrix([[self.m1, 0],
                       [0, self.m1*z**2+(1/3)*self.m2*self.l**2]])
        C = np.matrix([[self.m1*thetadot**2*z-self.m1*self.g*np.sin(theta)],
                       [F*self.l*np.cos(theta)-thetadot*2*self.m1*zdot*z-self.m1*self.g*z*np.cos(theta)-self.m2*self.g*(self.l/2)*np.cos(theta)]])
        
        tmp = np.linalg.inv(M)*C
        zddot = tmp.item(0)
        thetaddot = tmp.item(1)
        # build xdot and return
        xdot = np.matrix([[zdot], [thetadot], [zddot], [thetaddot]])
        return xdot

    def outputs(self):
        '''
            Returns the measured outputs as a list
            [z, theta] with added Gaussian noise
        '''
        # re-label states for readability
        z = self.state.item(0)
        theta = self.state.item(1)
        # add Gaussian noise to outputs
        z_m = z + random.gauss(0, 0.01)
        theta_m = theta + random.gauss(0, 0.001)
        # return measured outputs
        return [z_m, theta_m]

    def states(self):
        '''
            Returns all current states as a list
        '''
        return self.state.T.tolist()[0]