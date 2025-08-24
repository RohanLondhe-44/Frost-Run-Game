import pygame
import pygame_functions
import random
import math


screen = pygame.display.set_mode((900, 700))
pygame.init()
menu_font=pygame.font.SysFont('Comic Sans',100)
t_color=(0,0,0)
def print_text(text,font,t_color,x,y):
    img=font.render(text,True,t_color)
    screen.blit(img,(450,350))

run=True
while run:
    screen.fill((255,255,255))
