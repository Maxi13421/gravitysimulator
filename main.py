import time
import math

import pygame
from pygame.locals import *
import time

ACCURACY = 1e-3
SPEED = 1.0

def updateobj(staticobjects, dynamicobjects):
    window.fill((0,0,0))
    #comment for traces
    speed = SPEED
    highestforcesq = 0
    for aaa in dynamicobjects:
        forcecur = [0, 0]
        for aab in staticobjects+dynamicobjects:
            if(aab != aaa):
                forcecur[0] += aab.mass * (aab.pos[0] - aaa.pos[0]) / math.pow(math.pow(aab.pos[0] - aaa.pos[0], 2) + math.pow(aab.pos[1] - aaa.pos[1], 2), 1.5)
                forcecur[1] += aab.mass * (aab.pos[1] - aaa.pos[1]) / math.pow(math.pow(aab.pos[0] - aaa.pos[0], 2) + math.pow(aab.pos[1] - aaa.pos[1], 2), 1.5)
        aaa.force = forcecur
        absolutforcesq = pow(forcecur[0], 2) + pow(forcecur[1], 2)
        #print(absolutforcesq)
        if(absolutforcesq>highestforcesq):
            highestforcesq = absolutforcesq
    if(highestforcesq>pow(ACCURACY,2)):
        speed = ACCURACY / pow(highestforcesq,0.5) * SPEED
    for aaa in staticobjects:
        aaa.pos[0] += aaa.vel[0]*speed
        aaa.pos[1] += aaa.vel[1]*speed
        pygame.draw.circle(window, aaa.col, aaa.pos, aaa.size, 0)
    for aaa in dynamicobjects:
        aaa.vel[0] += aaa.force[0]*speed
        aaa.vel[1] += aaa.force[1]*speed
        aaa.pos[0] += aaa.vel[0]*speed
        aaa.pos[1] += aaa.vel[1]*speed
        #print(pow(pow(aaa.vel[0],2)+pow(aaa.vel[1],2),0.5))
        pygame.draw.circle(window, aaa.col, aaa.pos, aaa.size, 0)

    pygame.display.flip()
    #print(speed)

class object:
    def __init__(self, mass, pos, size, vel, col):
        self.mass = mass
        self.pos = pos
        self.size = size
        self.vel = vel
        self.col = col


if __name__ == '__main__':
    staticobjects = []
    dynamicobjects = []

    pygame.init()
    window = pygame.display.set_mode((800, 800))
    """
    #Sonnensystem
    dynamicobjects.append(object(2,[400,400], 20, [0,0],(255,255,0)))
    dynamicobjects.append(object(0.0006, [400, 800], 10, [0.0707,0], (0, 100, 100)))
    dynamicobjects.append(object(0.000000, [400, 794], 3, [0.082, 0], (100, 100, 100)))
    """
    """
    #Doppeldoppelsternsternsystem
    dynamicobjects.append(object(2,[000,400], 5, [0,0.06-0.071],(255,255,0)))
    dynamicobjects.append(object(2, [200, 400], 5, [0, 0.06+0.071], (255, 255, 0)))
    dynamicobjects.append(object(2, [600, 400], 5, [0, -0.06 - 0.071], (255, 255, 0)))
    dynamicobjects.append(object(2, [800, 400], 5, [0, -0.06 + 0.071], (255, 255, 0)))
    #staticobjects.append(object(0.01, [100, 400], 3, [0.00, 0.00], (0, 100, 100)))
    """
    """
    #Doppelstern statisch
    staticobjects.append(object(2, [300, 400], 20, [0, 0], (255, 255, 0)))
    staticobjects.append(object(2, [500, 400], 20, [0, 0], (255, 255, 0)))
    dynamicobjects.append(object(0.0006, [400, 700], 3, [0.09, 0], (0, 100, 100)))
    """
    """
    staticobjects.append(object(2, [400, 400], 20, [0, 0], (255, 255, 0)))
    dynamicobjects.append(object(0.0006, [400, 700], 3, [0.01, 0], (0, 100, 100)))
    """

    #gravitational catapult
    staticobjects.append(object(2, [400, 400], 20, [0, 0], (255, 255, 0)))
    dynamicobjects.append(object(0.1, [300, 400], 10, [0, 0.14], (0, 100, 100)))
    dynamicobjects.append(object(0.1, [700, 400], 10, [0, -0.08], (0, 100, 100)))
    dynamicobjects.append(object(0.00000001, [293, 400], 5, [0, -0.225], (100, 100, 100)))
    #dynamicobjects.append(object(2, [600, 400], 5, [0, -0.06 - 0.071], (255, 255, 0)))
    #dynamicobjects.append(object(2, [800, 400], 5, [0, -0.06 + 0.071], (255, 255, 0)))

    while(True):
        updateobj(staticobjects,dynamicobjects)
        #print(dynamicobjects[0].vel[1])
