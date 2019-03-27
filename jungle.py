from _settings import *
from Hero import hero
from platform import Platform
from levels import level1
def show_background():
    for img in bg:
        gamedisplay.blit(img, (0,0))

keys = {}
platforms = []
entities = pygame.sprite.Group()
x = y = 0
def drawPlatform():
    global platforms,x,y
    for line in level1:
        for simvol in line:
            if simvol == '-':
                p = Platform(x,y)
                platforms.append(p)
                entities.add(p)
            x += Platform.SIZE
        y += Platform.HIGH
        x = 0
drawPlatform()
game = True
while game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            keys[event.key] =  True
        if event.type == pygame.KEYUP:
            keys[event.key] = False
        if event.type == pygame.USEREVENT:
            show_background()

            entities.draw(gamedisplay)
            # entities.update()
            hero.update(keys)
    pygame.display.update()
pygame.quit()
