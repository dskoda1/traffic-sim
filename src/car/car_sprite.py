"""This module contains the sprite class that controls rendering of a car.
It defers decision making to the src.car.logic functions.
"""

import pygame
import math

from src.car import logic

from pygame.sprite import Sprite

class CarSprite(Sprite):
    """CarSprite is a pygame.Sprite subclass, and renders a car."""

    def __init__(self, image, position, screen):
        Sprite.__init__(self)
        self.src_image = pygame.transform.scale(pygame.image.load(image), (30, 20))
        self.src_image = pygame.transform.rotate(self.src_image, 90)
        self.position = position
        self.screen = screen
        self.speed = self.direction = 0
        self.lane = 0
        self.k_down = self.k_up = 0
        self.image = None
        self.rect = None
        self.last_action = 0


    def update(self, deltat):
        self.last_action += deltat
        # Can set how often a car will take an action with this
        if self.last_action > 2000:
            self.last_action = 0

        # Make decisions based on deltat
        if deltat:
            pass
        # Speed check
        self.speed = logic.calculate_speed(self.speed, self.k_up, self.k_down)

        # Only allowed to drive in one direction
        self.direction = 90

        # Unpack the position and update it
        x, y = self.position
        rad = self.direction * math.pi / 180
        if self.lane != 0:
            # self.lane is set to -1 or 1 for right/left
            y += self.lane * 10
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
        self.position = (x, y)
        self.image = pygame.transform.rotate(self.src_image, self.direction)
        self.rect = self.image.get_rect()
        self.rect.center = self.position
