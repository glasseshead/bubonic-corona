import os, sys, re

import config
import relativity

def cppRead():
    with open(os.path.join(os.path.dirname(__file__), 'path.cpp'), 'r') as f:
        content = f.read()

    # reset points list
    points = []
    
    # get offset from setPose
    offsetX, offsetY, offsetT = 0.0, 0.0, 0.0
    
    # find all moveToPose lines
    commands = re.finditer(r'chassis\.(setPose|moveToPose)\(([-\d.,\s]+)\)', content)
    
    for cmd in commands:
        cmd_type = cmd.group(1)
        params = [float(x.strip()) for x in cmd.group(2).split(',')]

        if cmd_type == 'moveToPose':
            # moveToPose at this offset position
            x, y, theta = params[0] + offsetX, params[1] + offsetY, params[2] + offsetT
            points.append({'x': x, 'y': y, 'theta': theta})
    
    return points