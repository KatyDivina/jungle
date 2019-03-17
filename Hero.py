from _settings import *
class Hero(pygame.sprite.Sprite):
#конструктор класса
    def __init__(self):
        self.animation()
        self.rect = self.image1.get_rect()
        self.rect.y = 0
        self.speed = 5
        self.isjump = False
        self.highofjump = 50
        self.countanimation = 0
    def update(self,keys):
        if self.countanimation == 9:
            self.countanimation = 0
        # if self.rect.x > SIZE:
        #     self.rect.x  = 0
        # else:
        #     self.rect.x += 1
        if keys.get(pygame.K_RIGHT):
            self.rect.x += self.speed
            self.countanimation += 1
            gamedisplay.blit(self.walk_Right[self.countanimation], self.rect)
        elif keys.get(pygame.K_LEFT):
            self.rect.x -= self.speed
            self.left_image1 =  pygame.transform.flip(self.left_image1,1,0)
            gamedisplay.blit(self.left_image1,self.rect)
        elif keys.get(pygame.K_SPACE):
            #self.rect.y -= 3
            self.jump()
        else:
            gamedisplay.blit(self.walk_Right[0],self.rect)
        if self.rect.bottom <= HIGH:
            self.rect.y += grav
    def jump(self):
        if self.rect.bottom >= HIGH:
            self.rect.y -= self.highofjump
        # if self.isjump == False:
        #     self.isjump = True
        #     self.rect.y  -= self.highofjump
        #     self.isjump = False
    def animation(self):
        #self.scale = 1
        self.image1 = pygame.image.load("images/walk1.png")
        self.image2 = pygame.image.load("images/walk2.png")
        self.image3 = pygame.image.load("images/walk3.png")
        self.image4 = pygame.image.load("images/walk4.png")
        self.image5 = pygame.image.load("images/walk5.png")
        self.image6 = pygame.image.load("images/walk6.png")
        self.image7 = pygame.image.load("images/walk7.png")
        self.image8 = pygame.image.load("images/walk8.png")
        self.image9 = pygame.image.load("images/walk9.png")
        self.image10 = pygame.image.load("images/walk10.png")
        self.left_image1 = pygame.image.load("images/left_walk1.png")
        self.walk_Right = [self.image1,self.image2,self.image3,self.image4,self.image5,self.image6,self.image7,self.image8,self.image9,self.image10,]
        self.walk_Left = self.walk_Right[:]
        #for e in range(10):
            #self.walk_Right[e] = pygame.transform.scale(self.walk_Right[e],(self.walk_Right[e].get_width()//self.scale,self.walk_Right[e].get_height()//self.scale))
    def move(self):
        for img in self.walk_Right:
            gamedisplay.blit(img,self.rect)
hero = Hero()
