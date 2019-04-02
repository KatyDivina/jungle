from _settings import *
from background import *

import Hero
hero = Hero.Hero()
entities.add(hero)

import platform
platform.drawPlatform(0, 0)


keys = {} #Словарь, в которм хранится информация о нажатых кнопках
game = True
while game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            keys[event.key] = True
        if event.type == pygame.KEYUP:
            keys[event.key] = False
        if event.type == pygame.USEREVENT:
            show_background()
            entities.draw(gamedisplay)
            entities.update(keys, hero)

    pygame.display.update()
pygame.quit()
