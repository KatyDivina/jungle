import pygame
import random
from background import *
pygame.init()
clock = pygame.time.Clock()   #Запуск игрового таймера
pygame.time.set_timer(pygame.USEREVENT,50) #Таймер, генерирующий раз в 50мс событие USEREVENT

entities = pygame.sprite.Group() #Группа всех игровых объектов
platforms = pygame.sprite.Group() #Группа всех игровых объектов
pygame.font.init()
font1 = pygame.font.SysFont(None,50)
font2 = pygame.font.SysFont('Comic Sans MS',150)

