"""This file will contain pure functions that are used in making decisions for
the car class. They should all remain pure in the sense that they don't hold
state for a CarSprite - those values should be passed in. This will allow these
functions to be tested thoroughly.
"""

class Speeds():
    MAX_FORWARD_SPEED = 10
    MAX_REVERSE_SPEED = 0
    ACCELERATION = 2
    TURN_SPEED = 5

def calculate_speed(current_speed, forward, backward):
    current_speed += forward + backward
    if current_speed > Speeds.MAX_FORWARD_SPEED:
        current_speed = Speeds.MAX_FORWARD_SPEED
    if current_speed < 0:
        current_speed = Speeds.MAX_REVERSE_SPEED
    return current_speed

