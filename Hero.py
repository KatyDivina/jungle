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

        self.speed = 5
        self.grav = 5

        self.isjump = False
        self.maxHighOfJump = 10
        self.highofjump = self.maxHighOfJump

    def update(self, keys):
        self.collide()
        print(self.rect.bottom,HIGH,self.stand)
        if self.stand == False:  # Гравитация
            self.rect.y += self.grav


        if self.countanimation == 9:  # Обнуление счётчика анимации(всего 10 изображений в списке)
            self.countanimation = 0

        if keys.get(pygame.K_RIGHT):  # движение вправо
            self.rect.x += self.speed
            self.countanimation += 1
            self.image = self.walk[self.countanimation]

        elif keys.get(pygame.K_LEFT):  # движение влево
            self.countanimation += 1
            self.rect.x -= self.speed
            self.image = self.walk[self.countanimation]
            self.image = pygame.transform.flip(self.image, 1, 0)

        if keys.get(pygame.K_SPACE) and self.stand:  # запуск прыжка
            self.isjump = True
            self.highofjump = self.maxHighOfJump

        if self.isjump:  # Продолжаем прыгать
            self.grav = 0
            self.jump()
        else:  # Окончание прыжка
            self.grav = 5

    def jump(self):

        if self.highofjump >= -self.maxHighOfJump:  # Jump
            sign = 1 if self.highofjump < 0 else -1
            self.rect.y += sign * (self.highofjump ** 2) // 2
            self.highofjump -= 1

        else:  # End of jump
            self.isjump = False
    def collide(self):
        print(self.rect.bottom,HIGH,self.stand,"d")
        if self.rect.bottom >= HIGH:
            self.stand = True
            self.rect.bottom = HIGH

        else:
            self.stand = False
            for p in platforms:
                if pygame.sprite.collide_rect(self,p):
                    if self.rect.bottom >= p.rect.top and self.rect.bottom <= p.rect.bottom:
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
