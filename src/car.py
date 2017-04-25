import pygame
import math

from pygame.sprite import Sprite


class CarSprite(Sprite):
    MAX_FORWARD_SPEED = 10
    MAX_REVERSE_SPEED = 0
    ACCELERATION = 2
    TURN_SPEED = 5

    def __init__(self, image, position, screen):
        Sprite.__init__(self)
        self.src_image = pygame.transform.scale(pygame.image.load(image), (30, 20))
        self.src_image = pygame.transform.rotate(self.src_image, 90)
        self.position = position
        self.screen = screen
        self.speed = self.direction = 0
        self.lane = 0
        self.k_left = self.k_right = self.k_down = self.k_up = 0

    def update(self, deltat):
        # Speed check
        self.speed += (self.k_up + self.k_down)
        if self.speed > self.MAX_FORWARD_SPEED:
            self.speed = self.MAX_FORWARD_SPEED
        if self.speed < 0:
            self.speed = self.MAX_REVERSE_SPEED

        # Set the cars direction
            
        #self.direction += self.k_right + self.k_left
        self.direction = 90

        # Unpack the position and update it
        x, y = self.position
        rad = self.direction * math.pi / 180
        if self.lane != 0:
            if self.lane == 1:
                y += 10
                self.lane = 0
            elif self.lane == -1:
                y -= 10
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

