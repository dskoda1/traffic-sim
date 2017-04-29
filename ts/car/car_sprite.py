"""This module contains the sprite class that controls rendering of a car.
It defers decision making to the src.car.logic functions.
"""

import pygame
import math
import random
from ts import RandomDecision

from ts.car import logic, config

from pygame.sprite import Sprite

class CarSprite(Sprite):
    """CarSprite is a pygame.Sprite subclass, and renders a car."""

    def __init__(self, image, position, screen, highway):
        Sprite.__init__(self)
        self.position = position
        self.screen = screen
        self.highway = highway

        # Car specific attributes
        self.src_image = pygame.transform.scale(pygame.image.load(image), (30, 20))
        self.src_image = pygame.transform.rotate(self.src_image, 90)
        self.speed = self.direction = 0
        self.lane = 0
        self.k_down = self.k_up = 0
        self.image = None
        self.rect = None
        self.last_action = 0

        self.aggressivity = random.randint(1, config.AGG_FACTOR)
        self.action_interval = random.randint(500, 2000)


    def update(self, deltat):
        self.last_action += deltat
        # Can set how often a car will take an action with this
        if self.last_action > self.action_interval:
            self.last_action = 0
            # This is the main routine of decision making for a car.
            # TODO: This will not act on things that happen frame by frame
            # it is only for making decisions that are not effected by
            # outside forces, every ACTION_INTERVAL.
            # Order of things to check for:
            # Speed not up to max speed, speed up.
            if self.speed == 0:
                self.speed = self.aggressivity
            else:
                lane = self.highway.lane(self.position[1])
                # attempt to switch lanes
                if lane > 0 and lane < self.highway.MAX_LANE -1:
                    self.lane = random.choice([1, -1])
                elif lane == 0:
                    self.lane = random.choice([1])
                elif lane == self.highway.MAX_LANE - 1:
                    self.lane = random.choice([-1])

        # Speed check

        # Only allowed to drive in one direction
        self.direction = 90

        # Unpack the position and update it
        x, y = self.position
        rad = self.direction * math.pi / 180
        if self.lane != 0:
            # self.lane is set to -1 or 1 for right/left
            y += self.lane * 20
            self.lane = 0

        x += -self.speed * math.sin(rad)
        #y += -self.speed * math.cos(rad)

        # Wrap the position so the car appears on the other side of the screen
        if x > self.screen.get_width():
            x = 0
        if x < 0:
            x = self.screen.get_width()
        if y > self.screen.get_height():
            y = 0
        if y < 0:
            y = self.screen.get_height()

        # Save the position,  rotate the image, and position the car
        self.position = x, y
        self.image = pygame.transform.rotate(self.src_image, self.direction)
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    @property
    def position(self):
        return self._x, self._y

    @position.setter
    def position(self, xy):
        self._x = xy[0]
        self._y = xy[1]
