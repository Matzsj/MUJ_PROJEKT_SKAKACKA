import sys
import pygame
import time
import random

pygame.init() 

rozliseni_vyska = 600
rozliseni_sirka = 800


screen = pygame.display.set_mode((rozliseni_sirka, rozliseni_vyska))


clock = pygame.time.Clock()  # Inicializace hodin


while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
      
    screen.fill((0, 0, 0))
            
            
            
            
    pygame.display.update()
    
    clock.tick(50) 