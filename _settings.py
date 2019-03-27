import pygame
import random
from background import *
pygame.init()
clock = pygame.time.Clock()   #Запуск игрового таймера
pygame.time.set_timer(pygame.USEREVENT,50) #Таймер, генерирующий раз в 50мс событие USEREVENT

entities = pygame.sprite.Group() #Группа всех игровых объектов
platforms = pygame.sprite.Group() #Группа всех игровых объектов

