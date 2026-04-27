import pygame

import config

def renderData(posX, posY, data, canvas):
    # set up text variables
    font = pygame.font.Font(None, 20)
    text = font.render(data, True, (255, 255, 255), (0, 0, 0))

    # blit text to canvas
    canvas.blit(text, (posX, posY))

def renderTiles(canvas):
    # render field perimeter
    pygame.draw.rect(canvas, (200, 200, 200), (140, 60, 520, 520))

    # may not be the best way to do this but hey i need to do something
    for i in range(6):
        for j in range(6):
            # checkerboard
            if ((j % 2 == 0 and i % 2 != 0) or
                (j % 2 != 0 and i % 2 == 0)): 
                pygame.draw.rect(canvas, (95, 95, 95), (160 + 80 * j, 80 + 80 * i, 80, 80))
            else:  
                pygame.draw.rect(canvas, (100, 100, 100), (160 + 80 * j, 80 + 80 * i, 80, 80))

def renderBot(robotPosX, robotPosY, robotPosTheta, canvas):
    # set surface for robot
    botSurf = pygame.Surface((70, 70), pygame.SRCALPHA)

    # draw robot and rotator indication
    pygame.draw.rect(botSurf, (255, 90, 90), (0, 0, 70, 70))
    pygame.draw.line(botSurf, (0, 0, 0), (70 // 2, 70 // 2), (70, 70 // 2), 4)

    # rotate transform
    rotated = pygame.transform.rotate(botSurf, -robotPosTheta)
    rotatedrect = rotated.get_rect(center = (robotPosX, robotPosY))

    # blit to canvas
    canvas.blit(rotated, rotatedrect)

def renderPath(points, canvas):
    if not points:
        return
    
    # convert points to screen coords and draw
    for i in range(len(points)):
        screenX = points[i]['x'] * config.tickPerIn + 160 + 40
        screenY = points[i]['y'] * config.tickPerIn + 80 + 40
        
        # draw line to previous point
        if i > 0:
            prevX = points[i - 1]['x'] * config.tickPerIn + 160 + 40
            prevY = points[i - 1]['y'] * config.tickPerIn + 80 + 40
            pygame.draw.line(canvas, (215, 255, 104), (prevX, prevY), (screenX, screenY), 3)
        
        # point for visibility
        pygame.draw.circle(canvas, (215, 255, 104), (int(screenX), int(screenY)), 5)

def renderField(canvas):
    # background
    canvas.fill(config.canvasBGColour)

    # render tiles, bot
    renderTiles(canvas)
    renderBot(config.robotPosX + 160, config.robotPosY + 80, config.robotPosTheta, canvas)

    # render planned points
    renderPath(config.pathPoints, canvas)