import numpy as np 
import random
import msdParam as S


class msdDynamics:
    '''
        Model the physical system
    '''

    def __init__(self):
        # Initial state conditions
        self.state = np.matrix([[S.z0],          # z initial position
                                [S.zdot0]])       # zdot initial velocity
                                 
        #################################################
        # The parameters for any physical system are never known exactly.  Feedback
        # systems need to be designed to be robust to this uncertainty.  In the simulation
        # we model uncertainty by changing the physical parameters by a uniform random variable
        # that represents alpha*100 % of the parameter, i.e., alpha = 0.2, means that the parameter
        # may change by up to 20%.  A different parameter value is chosen every time the simulation
        # is run.
        alpha = 0.2  # Uncertainty parameter
        self.m = S.m * (1+2*alpha*np.random.rand()-alpha)  # Mass of the cart, kg
        self.ell = S.ell * (1+2*alpha*np.random.rand()-alpha)  # Length of the rod, m
        self.b = S.b * (1+2*alpha*np.random.rand()-alpha)  # Damping coefficient, Ns
        self.g = S.g  # the gravity constant is well known and so we don't change it.
        self.k = S.k * (1+2*alpha*np.random.rand()-alpha) # K spring constant 

    def propagateDynamics(self, u):
        '''
            Integrate the differential equations defining dynamics
            P.Ts is the time step between function calls.
            u contains the system input(s).
        '''
        # Integrate ODE using Runge-Kutta RK4 algorithm
        k1 = self.derivatives(self.state, u)
        k2 = self.derivatives(self.state + S.Ts/2*k1, u)
        k3 = self.derivatives(self.state + S.Ts/2*k2, u)
        k4 = self.derivatives(self.state + S.Ts*k3, u)
        self.state += S.Ts/6 * (k1 + 2*k2 + 2*k3 + k4)

    def derivatives(self, state, u):
        '''
            Return xdot = f(x,u), the derivatives of the continuous states, as a matrix
        '''
        # re-label states and inputs for readability
        z = state.item(0)
        zdot = state.item(1)

        F = u[0]
        # The equations of motion.
        zddot = (1/self.m)*(F-self.b*zdot-self.k*z)

        # build xdot and return
        xdot = np.matrix([[zdot], [zddot]])
        return xdot

    def outputs(self):
        '''
            Returns the measured outputs as a list
            [z, theta] with added Gaussian noise
        '''
        # re-label states for readability
        z = self.state.item(0)
        #theta = self.state.item(1)
        # add Gaussian noise to outputs
        z_m = z + random.gauss(0, 0.01)
        #theta_m = theta + random.gauss(0, 0.001)
        # return measured outputs
        return [z_m]

    def states(self):
        '''
            Returns all current states as a list
        '''
        return self.state.T.tolist()[0]