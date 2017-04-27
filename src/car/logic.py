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

def calculate_speed(current_speed: int, forward: int, backward: int) -> int:
    """Provided a current speed, and a forward/backward change, calculate a
    new speed. Sets upper and lower bounds on the speed via constants.
    """
    current_speed += forward + backward
    if current_speed > Speeds.MAX_FORWARD_SPEED:
        current_speed = Speeds.MAX_FORWARD_SPEED
    if current_speed < 0:
        current_speed = Speeds.MAX_REVERSE_SPEED
    return current_speed
