from _settings import *


class Enemy(pygame.sprite.Sprite):
    # конструктор класса
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/скелет.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
enemy = Enemy(0,0)
entities.add(enemy)