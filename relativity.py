import config

def relativity():
    if len(config.poseData) == 1 or config.resetOrigin == True:
        config.originX, config.originY, config.originT = config.poseData[-1]
        # origin is the first point so it must be 0, 0, 0 relative
        config.relativeX = 0
        config.relativeY = 0
        config.relativeT = 0
        config.resetOrigin = False
    else:
        x, y, t = config.poseData[-1]
        # Divide by tickPerIn to convert pixels to inches and offset origin
        config.relativeX = (x - config.originX) / config.tickPerIn
        config.relativeY = (y - config.originY) / config.tickPerIn
        config.relativeT = t - config.originT