import pygame
import random
pygame.init()
clock=pygame.time.Clock()

#загрузка фонов
bg1 = pygame.image.load("background/plx-1.png")
bg2 = pygame.image.load("background/plx-2.png")
bg3 = pygame.image.load("background/plx-3.png")
bg4 = pygame.image.load("background/plx-4.png")
bg5 = pygame.image.load("background/plx-5.png")
HIGH=bg1.get_height()
SIZE=bg1.get_width()
gamedisplay = pygame.display.set_mode((SIZE, HIGH))
pygame.display.set_caption("Jungl")

grav = 1