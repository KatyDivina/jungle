from _settings import *
class Hero(pygame.sprite.Sprite):
#конструктор класса
    def __init__(self):
        self.animation()
        self.rect = self.walk[0].get_rect()
        self.rect.y = 200
        self.speed = 5
        self.img = self.walk[0]
        self.isjump = False
        self.highofjump = 10
        self.grav = 5
        self.countanimation = 0
    def update(self,keys):
        if self.countanimation == 9:
            self.countanimation = 0

        if keys.get(pygame.K_RIGHT):#движение в право
            self.rect.x += self.speed
            self.countanimation += 1
            self.img = self.walk[self.countanimation]
        elif keys.get(pygame.K_LEFT):#движение в лево
            self.countanimation += 1
            self.rect.x -= self.speed
            self.img = self.walk[self.countanimation]
            self.img =  pygame.transform.flip(self.img,1,0)

        elif keys.get(pygame.K_SPACE):#прыжок
            if self.rect.bottom >= HIGH:
                self.isjump = True
        if self.rect.bottom <= HIGH:
            self.rect.y += self.grav
        if self.isjump:
            self.jump()
        gamedisplay.blit(self.img, self.rect)

    def jump(self):
        self.grav = 0
        if self.highofjump >= -10:
            if self.highofjump < 0:
                self.rect.y +=(self.highofjump**2)//2
            else:
                self.rect.y -= (self.highofjump ** 2) // 2
            self.highofjump -= 1
        else:
            self.grav = 5
            self.isjump = False
            self.highofjump = 10

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
        self.walk_Left = self.walk[:]

    def move(self):
        for img in self.walk:
            gamedisplay.blit(img,self.rect)
hero = Hero()
