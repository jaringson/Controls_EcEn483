import vtolParamHW12_lat as P
import sys
sys.path.append('..')  # add parent directory
import vtolParam as P0
import numpy as np

class vtolController_lat:
    ''' 
        This class inherits other controllers in order to organize multiple controllers.
    '''

    def __init__(self):
        # Instantiates the SS_ctrl object


        self.z_dot = 0.0              # derivative of z
        self.theta_dot = 0.0          # derivative of theta
        self.z_d1 = 0.0              # Position z delayed by 1 sample
        self.theta_d1 = 0.0          # Angle theta delayed by 1 sample
        self.integrator = 0.0        # integrator
        self.error_d1 = 0.0          # error signal delayed by 1 sample
        self.K = P.K                 # state feedback gain
        self.ki = P.ki               # Input gain
        self.limit = P.tau_max         # Maxiumum force
        self.beta = P.beta           # dirty derivative gain
        self.Ts = P.Ts               # sample rate of controller

    def u(self, y_r, y):
        # y_r is the referenced input
        # y is the current state
        z_r = y_r[0]
        z = y[0]
        theta = y[2]


        # differentiate z and theta
        self.differentiateZ(z)
        self.differentiateTheta(theta)

        # integrate error
        error = z_r - z
        self.integrateError(error)

        # Construct the state
        x = np.matrix([[z], [theta], [self.z_dot], [self.theta_dot]])

        # Compute the state feedback controller
        tau_tilde = -self.K*x - self.ki*self.integrator
        tau_e = 0
        tau = tau_e + tau_tilde


        tau = self.saturate(tau)
        return [tau]

    def differentiateZ(self, z):
        '''
            differentiate z
        '''
        self.z_dot = self.beta*self.z_dot + (1-self.beta)*((z - self.z_d1) / self.Ts)
        self.z_d1 = z

    def differentiateTheta(self, theta):
        '''
            differentiate theta
        '''
        self.theta_dot = self.beta*self.theta_dot + (1-self.beta)*((theta - self.theta_d1) / self.Ts)
        self.theta_d1 = theta

    def integrateError(self, error):
        self.integrator = self.integrator + (self.Ts/2.0)*(error + self.error_d1)
        self.error_d1 = error

    def saturate(self, u):
        if abs(u) > self.limit:
            u = self.limit*np.sign(u)
        return u





