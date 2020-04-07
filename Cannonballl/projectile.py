"""
Provides a simple class for modeling the flight of projectiles
"""

from math import sin, cos, radians

"""
Simulates the flight of simple projectiles near the earth's surface, ignoring wind resistance. 
Tracking is done in two dimensions, height(y) and distance(x)
"""


class Projectile:
    def __init__(self, angle, velocity, height):
        """creates a projectile with given launch angles, initial velocities and height"""
        self.xpos = 0.0
        self.ypos = height
        theta = radians(angle)
        self.xvel = velocity * cos(theta)
        self.yvel = velocity * sin(theta)

    """Update the state of this projectile to move it " time " seconds farther into its flight"""

    def update(self, time):
        self.xpos = self.xpos + time * self.xvel
        yvel1 = self.yvel - 9.8 * time
        self.ypos - self.ypos + time * (self.yvel + yvel1) / 2.0
        self.yvel = yvel1

    """returns the y position ( height) of ths projectile"""

    def getY(self):
        return self.ypos

    """returns the x position ( distance) of this projectile"""

    def getX(self):
        return self.xpos
