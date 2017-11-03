import numpy as np 
import random
import vtolParam as V


class vtolDynamics:
    '''
        Model the physical system
    '''

    def __init__(self):
        # Initial state conditions
        self.state = np.matrix([[V.z0],         # z initial position
                                [V.h0],         # h initial position
                                [V.theta0],     # Theta initial orientation
                                [V.zdot0],      # zdot initial velocity
                                [V.hdot0],      # hdot initial velocity
                                [V.thetadot0],  # Thetadot initial velocity
                                [V.zt0]])
        #################################################
        # The parameters for any physical system are never known exactly.  Feedback
        # systems need to be designed to be robust to this uncertainty.  In the simulation
        # we model uncertainty by changing the physical parameters by a uniform random variable
        # that represents alpha*100 % of the parameter, i.e., alpha = 0.2, means that the parameter
        # may change by up to 20%.  A different parameter value is chosen every time the simulation
        # is run.
        alpha = 0.2  # Uncertainty parameter
        self.mr = V.mr #* (1+2*alpha*np.random.rand()-alpha)  # Mass of the right, kg
        self.ml = V.ml #* (1+2*alpha*np.random.rand()-alpha)  # Mass of the left, kg
        self.m = V.m #* (1+2*alpha*np.random.rand()-alpha) # Mass if m1 = m2, m
        self.mc = V.mc * (1+2*alpha*np.random.rand()-alpha) # Mass of the vtol body, kg
        
        self.mu = V.mu * (1+2*alpha*np.random.rand()-alpha)  # Viscous drag force, kg/s
        self.d = V.d * (1+2*alpha*np.random.rand()-alpha)  # Distance from prop to vtol body, m
        self.Jc = V.Jc * (1+2*alpha*np.random.rand()-alpha)  # Inertia of body, kg m**2
        self.g = V.g  # the gravity constant is well known and so we don't change it.


    def propagateDynamics(self, u):
        '''
            Integrate the differential equations defining dynamics
            B.Ts is the time step between function calls.
            u contains the system input(s).
        '''
        # Integrate ODE using Runge-Kutta RK4 algorithm
        k1 = self.derivatives(self.state, u)
        k2 = self.derivatives(self.state + V.Ts/2*k1, u)
        k3 = self.derivatives(self.state + V.Ts/2*k2, u)
        k4 = self.derivatives(self.state + V.Ts*k3, u)
        self.state += V.Ts/6 * (k1 + 2*k2 + 2*k3 + k4)

    def derivatives(self, state, u):
        '''
            Return xdot = f(x,u), the derivatives of the continuous states, as a matrix
        '''
        # re-label states and inputs for readability
        z = state.item(0)
        h = state.item(1)
        theta = state.item(2)
        zdot = state.item(3)
        hdot = state.item(4)
        thetadot = state.item(5)
        Fr = u[0]
        Fl = u[1] 
        # The equations of motion.

        M = np.matrix([[2*self.m+self.mc, 0, 0],
                       [0, 2*self.m+self.mc, 0],
                       [0, 0, 2*self.m*self.d**2+self.Jc]])
        C = np.matrix([[(-(Fr+Fl)*np.sin(theta)-self.mu*zdot)],
                       [(Fr+Fl)*np.cos(theta)-(self.mc+2*self.m)*self.g],
                       [(Fr-Fl)*self.d]])
        
        tmp = np.linalg.inv(M)*C
        zddot = tmp.item(0)
        hddot = tmp.item(1)
        thetaddot = tmp.item(2)
        # build xdot and return
        xdot = np.matrix([[zdot], [hdot], [thetadot], [zddot], [hddot], [thetaddot], [V.zt0]])
        return xdot

    def outputs(self):
        '''
            Returns the measured outputs as a list
            [z, theta] with added Gaussian noise
        '''
        # re-label states for readability
        h = self.state.item(1)
        
        # add Gaussian noise to outputs
        h_m = h + random.gauss(0, 0.01)
        # return measured outputs
        return [h_m]

    def states(self):
        '''
            Returns all current states as a list
        '''
        return self.state.T.tolist()[0]