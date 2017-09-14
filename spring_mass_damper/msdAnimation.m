classdef msdAnimation
    %
    %    Create pendulum animation
    %
    %--------------------------------
    properties
        base_handle
        damper_handle
        spring_handle
        ell
        width
        height
        gap
        radius
    end
    %--------------------------------
    methods
        %------constructor-----------
        function self = msdAnimation(P)
            self.ell = P.ell;
            self.width = P.w;
            self.height = P.h;
            self.gap = P.gap;
            
            figure(1), clf
            plot([-2*self.ell, 2*self.ell],[0,0],'k'); % draw track
            hold on
            plot([-2,0],[-2*self.ell, 2*self.ell],'k'); % draw wall
            
            % initialize the base, rod, and bob to initial conditions
            self=self.drawBase(P.z0);
            self=self.drawSpring(P.z0);
            self=self.drawDamper(P.z0);
            axis([-3*self.ell, 3*self.ell, -0.1, 3*self.ell]); % Change the x,y axis limits
            xlabel('z'); % label x-axis
        end
        %---------------------------
        function self=drawMSD(self, x)
            % Draw pendulum is the main function that will call the functions:
            % drawCart, drawCircle, and drawRod to create the animation.
            % x is the system state
            z= x(1);        % Horizontal position of cart, m

            self=self.drawBase(z);
            self=self.drawDamper(z);
            self=self.drawSpring(z);
            drawnow
        end
        %---------------------------
        function self=drawBase(self, z)
            pts = [...
                z-self.width/2, self.gap;...
                z+self.width/2, self.gap;...
                z+self.width/2, self.gap+self.height;...
                z-self.width/2, self.gap+self.height;...
                ];

            if isempty(self.base_handle)
                self.base_handle = fill(pts(:,1),pts(:,2),'b');
            else
                set(self.base_handle,'XData',pts(:,1));
            end
        end
        %---------------------------
        function self=drawDamper(self, z)
            X = [z, z+self.ell*sin(theta)]; % X data points
            Y = [...
                self.gap+self.height,...
                self.gap + self.height + self.ell*cos(theta)...
                ]; % Y data points

            if isempty(self.damper_handle)
                self.damper_handle = plot(X, Y, 'k');
            else
                set(self.damper_handle,'XData', X, 'YData', Y);
            end
        end
        %---------------------------
        function self=drawSpring(self, z)
            th = 0:2*pi/10:2*pi;
            center = [...
                z + (self.ell+self.radius)*sin(theta),...
                self.gap+self.height+(self.ell+self.radius)*cos(theta)...
                ];
            pts = center + [self.radius*cos(th)', self.radius*sin(th)'];

            if isempty(self.spring_handle)
                self.spring_handle = fill(pts(:,1),pts(:,2),'g');
            else
                set(self.spring_handle,'XData',pts(:,1));
                set(self.spring_handle,'YData',pts(:,2));
            end
        end 
    end
end