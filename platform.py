from _settings import entities, platforms,SIZE
from levels import level1
import pygame
from Hero import hero
from enemy import *

class Platform(pygame.sprite.Sprite):
    HIGH = 50
    SIZE = 150

    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)

        self.HIGH = Platform.HIGH
        self.SIZE = Platform.SIZE

        self.image = pygame.Surface((self.SIZE,self.HIGH))
        self.image.fill((0, 255, 119))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, keys):
        if hero.rect.centerx > SIZE // 2:
            self.rect.x -= 3

            # hero.rect.x -= 1
    # self.image.fill((0, 255, 119))
    def change_color(self,color):
        self.image.fill(color)
        #self.rect.y+= 1




platforms_list = []

def drawPlatform(x, y):
    startX, startY = x, y

    for line in level1:
        for simvol in line:
            if simvol == '-':
                p = Platform(x,y)
                platforms_list.append(p)
                entities.add(p)
                platforms.add(p)
            if simvol == '+':
                p = Platform(x, y)
                platforms_list.append(p)
                entities.add(p)
                platforms.add(p)
                e = Enemy(p.rect.centerx,p.rect.top)
                entities.add(e)
            x += Platform.SIZE
        y += Platform.HIGH
        x = startX


drawPlatform(0, 0)
