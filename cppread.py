import os, sys, re

import config
import relativity

def cppRead():
    with open(os.path.join(os.path.dirname(__file__), 'path.cpp'), 'r') as f:
        content = f.read()

    # reset points list
    points = []
    
    # get offset from ZERO command
    config.offsetX, config.offsetY, config.offsetT = 0.0, 0.0, 0.0
    zero = re.search(r'//\s*ZERO\s+([-\d.]+)\s+([-\d.]+)\s+([-\d.]+)', content)
    if zero:
        config.offsetX = float(zero.group(1))
        config.offsetY = float(zero.group(2))
        config.offsetT = float(zero.group(3))

    # find all moveToPose lines
    commands = re.finditer(r'chassis\.(moveToPose)\(([-\d.,\s]+)\)', content)
    
    for cmd in commands:
        cmd_type = cmd.group(1)
        params = [float(x.strip()) for x in cmd.group(2).split(',')]

        if cmd_type == 'moveToPose':
            # moveToPose at this offset position
            x, y, theta = params[0] + config.offsetX, params[1] + config.offsetY, params[2] + config.offsetT
            points.append({'x': x, 'y': y, 'theta': theta})
    
    return points