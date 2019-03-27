from _settings import gamedisplay, entities
from levels import level1
import pygame


class Platform(pygame.sprite.Sprite):
    HIGH = 100
    SIZE = 100
    def __init__(self,x,y):
        self.HIGH = 100
        self.SIZE = 100
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((self.SIZE,self.HIGH))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image.fill((0,255,119))
    def update(self):
        gamedisplay.blit(self.image,self.rect)


platforms = []



def drawPlatform(x, y):
    global platforms
    for line in level1:
        for simvol in line:
            if simvol == '-':
                p = Platform(x,y)
                platforms.append(p)
                entities.add(p)
            x += Platform.SIZE
        y += Platform.HIGH
        x = 0
drawPlatform(0, 0)
