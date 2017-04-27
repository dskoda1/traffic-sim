# INTIALISATION
import pygame, sys
from pygame.locals import *
from src.car import CarSprite
from src.highway import HighwayDrawer

screen = pygame.display.set_mode((1024, 768), pygame.RESIZABLE)
pygame.display.set_caption('Traffic sim')
clock = pygame.time.Clock()
white = (255,255,255)
# CREATE A CAR AND RUN
rect = screen.get_rect()
car = CarSprite('img/car-top.png', rect.center, screen)
highway = HighwayDrawer(screen)
car_group = pygame.sprite.RenderPlain(car)
pygame.display.update()
while 1:
    deltat = clock.tick(30)
    for event in pygame.event.get():
        if not hasattr(event, 'key'): continue
        down = event.type == KEYDOWN

        if event.key == K_RIGHT:
            car.k_down = down * -2
            car.lane = 0
        elif event.key == K_LEFT:
            car.k_up = down * 2
            car.lane = 0
        elif event.key == K_UP:
            car.lane = -1
        elif event.key == K_DOWN:
            car.lane = 1
        elif event.key == K_ESCAPE: sys.exit(0)


    screen.fill((145, 145, 145))
    highway.draw()
    car_group.update(deltat)
    car_group.draw(screen)
    pygame.display.flip()
