from _settings import *


class Hero(pygame.sprite.Sprite):
    # конструктор класса
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.animation()
        self.countanimation = 0
        self.image = self.walk[self.countanimation]

        self.rect = self.walk[0].get_rect()
        self.rect.bottom = HIGH
        self.stand = True

        self.speedx = 5
        self.speedy = 0
        self.grav = 5

        self.isjump = False
        self.maxHighOfJump = 50
        self.highofjump = self.maxHighOfJump

    def update(self, keys):
        self.collide()
        if self.stand:  # Стоит
            self.isjump = False
            self.speedx = 5
            self.speedy = 0
        else:           #Падает
            self.speedy += self.grav


        if self.countanimation == 9:  # Обнуление счётчика анимации(всего 10 изображений в списке)
            self.countanimation = 0

        if keys.get(pygame.K_RIGHT):  # движение вправо
            self.rect.x += self.speedx
            self.countanimation += 1
            self.image = self.walk[self.countanimation]

        elif keys.get(pygame.K_LEFT):  # движение влево
            self.countanimation += 1
            self.rect.x -= self.speedx
            self.image = self.walk[self.countanimation]
            self.image = pygame.transform.flip(self.image, 1, 0)

        if keys.get(pygame.K_SPACE) and self.stand:  # запуск прыжка
            self.speedx += 5
            self.isjump = True
            self.speedy = -self.maxHighOfJump
        self.rect.y += self.speedy

    def collide(self):
        if self.rect.bottom >= HIGH + 20:#мы провалились
            self.stand = True
            self.rect.bottom = HIGH + 1000
            bonus_text = font2.render("game over ", True, (255, 0, 0))
            gamedisplay.blit(bonus_text,(200,200))
        else:
            self.stand = False
            for p in platforms:
                if pygame.sprite.collide_rect(self,p):
                    if p.rect.bottom >= self.rect.bottom >= p.rect.top:
                        if p.rect.left <= self.rect.centerx <= p.rect.right:
                            self.stand = True
                            self.isjump = False
                            self.rect.bottom = p.rect.top + 5
                            p.change_color((0,255,0))




    def animation(self):
        self.walk = []
        self.walk.append(pygame.image.load("images/walk1.png"))
        self.walk.append(pygame.image.load("images/walk2.png"))
        self.walk.append(pygame.image.load("images/walk3.png"))
        self.walk.append(pygame.image.load("images/walk4.png"))
        self.walk.append(pygame.image.load("images/walk5.png"))
        self.walk.append(pygame.image.load("images/walk6.png"))
        self.walk.append(pygame.image.load("images/walk7.png"))
        self.walk.append(pygame.image.load("images/walk8.png"))
        self.walk.append(pygame.image.load("images/walk9.png"))
        self.walk.append(pygame.image.load("images/walk10.png"))


hero = Hero()
entities.add(hero)
