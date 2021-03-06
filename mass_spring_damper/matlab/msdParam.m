% Inverted Pendulum Parameter File

% Physical parameters of the inverted pendulum known to the controller
P.m2 = 1.0;      % Mass of the box, kg
P.ell = 0.5;    % Length of the rod, m
P.k = 9.8;       % Spring constant
P.b = 0.05;      % Damping coefficient, Ns

% parameters for animation
P.w = 0.5;       % Width of the box, m
P.h = 0.15;      % Height of the box, m
P.gap = 0.005;   % Gap between the box and x-axis

% initial conditions
P.z0 = 0;         % initial position of cart in m
P.zdot0 = 0;      % initial velocity of cart in m/s
P.theta0 = 0;     % initial angle of rod in rad
P.thetadot0 = 0;  % initial angular velocity of rod in rad/sec

% Simulation parameters
P.t_start = 0.0;  % Start time of simulation
P.t_end = 50.0;   % End time of simulation
P.Ts = 0.01;      % sample time for controller
P.t_plot = 0.1;   % the plotting and animation is updated at this rate

% dirty derivative parameters
P.sigma = 0.05; % cutoff freq for dirty derivative
P.beta = (2*P.sigma-P.Ts)/(2*P.sigma+P.Ts); % dirty derivative gain

% control saturation limits
P.F_max = 5; % Max Force, N
