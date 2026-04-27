import config

def bounds():
    # set bounds for robot to fallback to
    if (config.robotPosX < 36): config.robotPosX = 36
    if (config.robotPosX > 444): config.robotPosX = 444

    if (config.robotPosY < 36): config.robotPosY = 36
    if (config.robotPosY > 444): config.robotPosY = 444