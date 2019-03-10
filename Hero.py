from _settings import *
class Hero(pygame.sprite.Sprite):
#конструктор класса
    def __init__(self):
        self.image = pygame.image.load("Hero/landing.png")
        self.rect = self.image.get_rect()
        self.rect.y = 0.75*HIGH
        self.speed = 2
    def update(self,keys):
        # if self.rect.x > SIZE:
        #     self.rect.x  = 0
        # else:
        #     self.rect.x += 1
        if keys.get(pygame.K_RIGHT):
            self.rect.x += self.speed
        if keys.get(pygame.K_LEFT):
            self.rect.x -= self.speed
        if keys.get(pygame.K_SPACE):
            self.rect.y -= 3
        if self.rect.bottom != HIGH:
            self.rect.y += grav
        gamedisplay.blit(self.image,self.rect)
hero = Hero()