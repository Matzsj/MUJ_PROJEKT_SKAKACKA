import sys
import pygame 

# Inicializace Pygame
pygame.init() 

# Nastavení rozlišení
rozliseni_vyska = 600
rozliseni_sirka = 800

# Vytvoření okna
screen = pygame.display.set_mode((rozliseni_sirka, rozliseni_vyska))

# Pokus o načtení obrázku
try:
    background_image = pygame.image.load('backgroundColorForest.png')
    background_image = pygame.transform.scale(background_image, (rozliseni_sirka, rozliseni_vyska))
except pygame.error as e:
    print(f"Chyba při načítání obrázku: {e}")
    pygame.quit()
    sys.exit()

# Hlavní herní cyklus
while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()   

    # Vykreslení pozadí
    screen.blit(background_image, (0, 0))

    # Aktualizace obrazovky
    pygame.display.update()
