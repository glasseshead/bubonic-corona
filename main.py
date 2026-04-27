import pygame, sys, os
from pygame.locals import *
import config

import render
import relativity
import boundary
import cppread

# initialize
pygame.init()

# set clock

# set up canvas
canvas = pygame.display.set_mode((config.canvasX, config.canvasY))
pygame.display.set_caption('Corona for Bubonic')

# read path from path.cpp
config.pathPoints = cppread.cppRead()

while True:
    # getting raw mouse values
    config.mouseXraw, config.mouseYraw = pygame.mouse.get_pos()

    # to prevent theta getting too high
    config.robotPosTheta = config.robotPosTheta % 360
    
    # boundary check
    boundary.bounds()

    # relativity
    if len(config.poseData) >= 1:
        relativity.relativity()

    # control loop
    for event in pygame.event.get():
        # exit control
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    # render field
    render.renderField(canvas)

    # update ticks
    pygame.display.update()
    config.fpsClock.tick(config.fps)