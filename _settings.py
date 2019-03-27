import pygame
import random
pygame.init()
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT,50)

#загрузка фонов
bg= []

bg.append(pygame.image.load("background/plx-1.png"))
bg.append(pygame.image.load("background/plx-2.png"))
bg.append(pygame.image.load("background/plx-3.png"))
bg.append(pygame.image.load("background/plx-4.png"))
bg.append(pygame.image.load("background/plx-5.png"))


SCALE = 3
HIGH= bg[1].get_height()  * SCALE
SIZE= bg [1]  .get_width() * SCALE

gamedisplay = pygame.display.set_mode((SIZE, HIGH))
pygame.display.set_caption("Jungle")


for i in range(len(bg)):
    bg[i] = pygame.transform.scale(bg[i].convert_alpha(), (SIZE, HIGH))