import math
from math import radians, cos, sin

"""
def main():
    angle, vel, h0, time = getInputs()
    xpos, ypos = 0, h0
    xvel, yvel = getXYComponents(vel, angle)
    # loop until the ball hits the ground
    # calculate position and velocity in time seconds
    while ypos >= 0:
        xpos, ypos, yvel = updateCannonBall(time, xpos, ypos, xvel, yvel)
    print("\nDistance traveled: {0:0.1f} meters.".format(xpos))
"""


def main():
    angle, vel, h0, time = getInputs()
    cball = Projectile(angle, vel,
                       h0)  # we stopped here where we will make anew class for the projectike and the new var.. cball at pg 320
    while cball.getY() >= 0:
        print(print("\nDistance traveled: {0:0.1f} meters.".format(cball.getX())))


def getInputs(angle, vel, h0, time):
    angle = float(input("Enter the launch angle( in degrees): "))
    vel = float(input("Enter the initial velocity (in meters/sec): "))
    h0 = float(input("Enter the initial height (in meters) :"))
    time = float(input("Enter the time interval between position calculation: "))
    return angle, vel, h0, time

    # convert angle to radians
    # set the initial position and velocities in x and y directions


def getXYComponents(vel, angle):
    theta = radians(angle)
    xvel = vel * cos(theta)
    yvel = vel * sin(theta)
    return xvel, yvel


def updateCannonBall(time, xpos, ypos, xvel, yvel):
    xpos = xpos + time * xvel
    yvel1 = yvel - time * 9.8
    ypos = ypos + time * (yvel + yvel1) / 2.0
    yvel = yvel1
    return xpos, yvel, ypos


class Projectile:
    def __init__(self, angle, velocity, height):
        self.xpos = 0.0
        self.ypos = 0.0
        theta = math.radians(angle)
        self.xvel = velocity * math.cos(theta)
        self.yvel = velocity * math.sin(theta)

    def getX(self):
        return self.xpos

    def getY(self):
        return self.ypos

    def update(self, time):
        self.xpos = self.xpos + time * self.xvel
        yvel1 = self.yvel - time * 9.8
        self.ypos = self.ypos + time * (self.yvel + yvel1) / 2.0
        self.yvel = yvel1
