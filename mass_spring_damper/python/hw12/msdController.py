import numpy as np
import msdParamHW12 as P
import sys
sys.path.append('..')  # add parent directory
import msdParam as P0


class msdController:

    def __init__(self):

        self.z_dot = 0.0          # derivative of theta
        self.z_d1 = 0.0          # Angle theta delayed by 1 sample
        self.integrator = 0.0        # integrator
        self.error_d1 = 0.0          # error signal delayed by 1 sample
        self.K = P.K                 # state feedback gain
        self.ki = P.ki               # Input gain
        self.limit = P0.F_max         # Maxiumum force
        self.beta = P.beta           # dirty derivative gain
        self.Ts = P.Ts               # sample rate of controller

    def u(self, y_r, y):
        # y_r is the referenced input
        # y is the current state
        z_r = y_r[0]
        z = y[0]

        # differentiate theta
        self.differentiateZ(z)

        # integrate error
        error = z_r - z
        self.integrateError(error)

        # Construct the state
        x = np.matrix([[z], [self.z_dot]])

        # compute equilibrium torque tau_e
        F_e = P0.k * z

        # Compute the state feedback controller
        F_tilde = -self.K*x - self.ki*self.integrator

        # compute total torque
        F = F_e + F_tilde
        F = self.saturate(F)
        return [F]


    def differentiateZ(self, z):
        '''
            differentiate z
        '''
        self.z_dot = self.beta*self.z_dot + (1-self.beta)*((z- self.z_d1) / self.Ts)
        self.z_d1 = z

    def integrateError(self, error):
        self.integrator = self.integrator + (self.Ts/2.0)*(error + self.error_d1)
        self.error_d1 = error

    def saturate(self, u):
        if abs(u) > self.limit:
            u = self.limit*np.sign(u)
        return u







