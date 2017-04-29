# INTIALISATION
import pygame, sys
from pygame.locals import *
from ts.car import CarSprite
from ts.highway import HighwayDrawer

screen = pygame.display.set_mode((1024, 768), pygame.RESIZABLE)
pygame.display.set_caption('Traffic sim')
clock = pygame.time.Clock()
white = (255,255,255)
pygame.font.init()


def text_to_screen(screen, text, x, y, size = 50):
    color = (200, 000, 000)
    try:
        text = str(text)
        font = pygame.font.Font(None, size)
        text = font.render(text, True, color)
        screen.blit(text, (x, y))
    except Exception as e:
        print('Font Error, saw it coming')
        raise

rect = screen.get_rect()
highway = HighwayDrawer(screen)
cars = []
for x in range(5):
    c_x, c_y = rect.center
    car = CarSprite('img/car-top.png', (c_x, c_y + 20 * x), screen, highway)
    cars.append(car)
car_group = pygame.sprite.RenderPlain(cars)
pygame.display.update()
while 1:
    deltat = clock.tick(30)
    for event in pygame.event.get():
        if not hasattr(event, 'key'): continue
        down = event.type == KEYDOWN

        if event.key == K_ESCAPE: sys.exit(0)


    screen.fill((145, 145, 145))
    highway.draw()
    car_group.update(deltat)
    car_group.draw(screen)
    text_to_screen(screen, 'hello', 0, 10)
    pygame.display.flip()

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

