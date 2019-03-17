from _settings import *
from Hero import hero
def show_background():
    for i in range(len(bg)):
        gamedisplay.blit(bg[i], (0,0))

keys = {}

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
            hero.update(keys)

    pygame.display.update()
pygame.quit()
