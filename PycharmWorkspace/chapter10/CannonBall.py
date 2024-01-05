"""
is a rough outline:
input the simulation parameters: angle , velocity , height , interval
calculate the initial position of the cannonball: xpos , ypos
calculate the initial velocities of the cannonball: xvel , yvel
while the cannonball is still flying:
update the values of xpos , ypos , and yvel for interval seconds
further into the flight
output the distance traveled as xpos
"""
from math import radians, cos, sin, pi



def cmain():
    angle = eval(input("Enter the launch angle (in degrees): "))
    vel = eval(input("Enter the initial velocity (in meters/sec): "))
    h0 = eval(input("Enter the initial height (in meters): "))
    time = eval(input("Enter the time interval between position calculations: "))

    radians = (angle * pi) / 180.0
    xpos = 0
    ypos = h0
    xvel = vel * cos(radians)
    yvel = vel * sin(radians)
    while ypos >= 0:
        xpos = xpos + time * xvel
        yvel1 = yvel - 9.8 * time
        ypos = ypos + time * (yvel + yvel1) / 2.0
        yvel = yvel1

    print("\nDistance traveled: {0:0.1f} meters.".format(xpos))

def dmain():
    angle, vel,hO,time = getInputs()
    xpos,ypos = O,hO
    xvel,yvel = getXYComponents(vel,angle)
    while ypos>= 0:
        xpos,ypos,yvel = updateCannonBall(time,xpos,ypos,xval,yval)

    print("\nDistance travled: {0:0.1f} meters.".format(xpos)  )




def getInput(angle,vel,hO,time):
    angle = 30
    vel = 50
    h0 = 3
    time = 10



def main():
    angle,vel,hO,time = getInput()
    cball = Projectiles(angle,vel,hO)
    while cball.getY() >=0:
        cball.updates(time)
        print("\nDistance travled: {0:0.1f} meters.".format(cball.getX()))

main()

class Projectiles:
    def __init__(self,angle,velocity,height):
        self.xpos = 0.0
        self.ypos = height
        theta = pi * angle / 180.0
        self.xvel = velocity * cos(theta)
        self.yvel = velocity * sin(theta)

    def getY(self):
            return self.ypos
    def getX(self):
        return self.xpos
    def update(self,time):
        self.xpos = self.xpos + time * self.xvel
        yvel1 = self.yvel - 9.8 * time
        self.ypos = self.ypos + time * (self.yvel + yvel1) / 2.0
        self.yvel = yvel1
