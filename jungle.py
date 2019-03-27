from _settings import *
from Hero import hero
from platform import Platform

keys = {} #Словарь, в которм хранится информация о нажатых кнопках

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
