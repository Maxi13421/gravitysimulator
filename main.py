import time
import math

import pygame
from pygame.locals import *
import time

def updateobj(staticobjects, dynamicobjects):
    #window.fill((0,0,0))
    #comment for traces
    for aaa in dynamicobjects:
        force = [0, 0]
        for aab in staticobjects+dynamicobjects:
            if(aab != aaa):
                force[0] += aab.mass*(aab.pos[0]-aaa.pos[0])/math.pow(math.pow(aab.pos[0]-aaa.pos[0],2)+math.pow(aab.pos[1]-aaa.pos[1],2),1.5)
                force[1] += aab.mass * (aab.pos[1] - aaa.pos[1]) / math.pow(math.pow(aab.pos[0] - aaa.pos[0], 2) + math.pow(aab.pos[1] - aaa.pos[1], 2), 1.5)
        aaa.vel[0] += force[0]/4
        aaa.vel[1] += force[1]/4
        aaa.pos[0] += aaa.vel[0]
        aaa.pos[1] += aaa.vel[1]
        pygame.draw.circle(window, aaa.col, aaa.pos, aaa.size, 0)
    for aaa in staticobjects:
        aaa.pos[0] += aaa.vel[0]
        aaa.pos[1] += aaa.vel[1]
        pygame.draw.circle(window, aaa.col, aaa.pos, aaa.size, 0)
    pygame.display.flip()

class object:
    def __init__(self, mass, pos, size, vel, col):
        self.mass = mass
        self.pos = pos
        self.size = size
        self.vel = vel
        self.col = col


if __name__ == '__main__':
    SPEED = 0.1
    staticobjects = []
    dynamicobjects = []
    pygame.init()
    window = pygame.display.set_mode((800, 800))
    """
    #Sonnensystem
    dynamicobjects.append(object(2,[400,400], 20, [0,0],(255,255,0)))
    dynamicobjects.append(object(0.0006, [400, 800], 10, [0.03535,0], (0, 100, 100)))
    dynamicobjects.append(object(0.000000, [400, 794], 3, [0.041, 0], (100, 100, 100)))
    """
    """
    #Doppeldoppelsternsternsystem
    dynamicobjects.append(object(2,[000,400], 5, [0,0.03-0.0355],(255,255,0)))
    dynamicobjects.append(object(2, [200, 400], 5, [0, 0.03+0.0355], (255, 255, 0)))
    dynamicobjects.append(object(2, [600, 400], 5, [0, -0.03 - 0.0355], (255, 255, 0)))
    dynamicobjects.append(object(2, [800, 400], 5, [0, -0.03 + 0.0355], (255, 255, 0)))
    """
    #Doppelstern statisch
    staticobjects.append(object(2, [300, 400], 20, [0, 0], (255, 255, 0)))
    staticobjects.append(object(2, [500, 400], 20, [0, 0], (255, 255, 0)))
    dynamicobjects.append(object(0.0006, [400, 700], 3, [0.045, 0], (0, 100, 100)))

    while(True):
        updateobj(staticobjects,dynamicobjects)
        #print(dynamicobjects[0].vel[1])
