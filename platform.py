from _settings import gamedisplay, entities
from levels import level1
import pygame


class Platform(pygame.sprite.Sprite):
    HIGH = 100
    SIZE = 100

    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)

        self.HIGH = Platform.HIGH
        self.SIZE = Platform.SIZE

        self.image = pygame.Surface((self.SIZE,self.HIGH))
        self.image.fill((0, 255, 119))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, *args):
        pass



platforms = []

def drawPlatform(x, y):
    startX, startY = x, y

    for line in level1:
        for simvol in line:
            if simvol == '-':
                p = Platform(x,y)
                platforms.append(p)
                entities.add(p)
            x += Platform.SIZE
        y += Platform.HIGH
        x = startX


drawPlatform(0, 0)
