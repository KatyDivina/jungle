from _settings import *
from Hero import hero
def show_background():
    gamedisplay.blit(bg1, (0,0))
    gamedisplay.blit(bg5, (0,0))
    gamedisplay.blit(bg2, (0,0))
    gamedisplay.blit(bg3, (0,0))
    gamedisplay.blit(bg4, (0,0))
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
    show_background()
    hero.update(keys)
    pygame.display.update()
pygame.quit()
