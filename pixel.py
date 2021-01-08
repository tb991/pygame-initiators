import pygame
import sys
# thanks to https://sites.cs.ucsb.edu/~pconrad/cs5nm/topics/pygame/drawing/

pygame.init()
             
screen = pygame.display.set_mode((640,480))

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)

while 1:
    screen.fill(green)

    pygame.display.update()
    a = input("")
    screen.fill(red)

    pygame.display.update()

    a = input("")
    screen.fill(blue)

    pygame.display.update()
    a = input("")
