from _settings import *


class Enemy(pygame.sprite.Sprite):
    # конструктор класса
    def __init__(self,p):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/скелет.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = p.rect.centerx
        self.rect.bottom = p.rect.top
        self.platform = p

    def update(self, *args):
        self.rect.centerx = self.platform.rect.centerx

