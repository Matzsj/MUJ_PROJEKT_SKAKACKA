import sys
import pygame 

# Inicializace Pygame
pygame.init() 

# Rozlišení okna
rozliseni_vyska = 600
rozliseni_sirka = 800

# Vlastnosti postavy
rychlost = 5
vyska_skoku = -14
gravitace = 1
y_velocity = 0
pozice_x_hrace = 100
pozice_y_hrace = 90
skace = False
zem = 90  # Výška země

# Vytvoření okna
screen = pygame.display.set_mode((rozliseni_sirka, rozliseni_vyska))

# Načtení obrázku pozadí
try:
    background_image = pygame.image.load('backgroundColorForest.png')
    background_image = pygame.transform.scale(background_image, (rozliseni_sirka, rozliseni_vyska))
except pygame.error as e:
    print(f"Chyba při načítání obrázku: {e}")
    pygame.quit()
    sys.exit()

# Načtení obrázku postavy
try:
    postava = pygame.image.load('ufo-removebg-preview.png').convert_alpha()
except pygame.error as e:
    print(f"Chyba při načítání obrázku postavy: {e}")
    pygame.quit()
    sys.exit()

# Herní smyčka
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()   
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not skace:  # Skok jen když nestojíme ve vzduchu
                y_velocity = vyska_skoku
                skace = True

    # Pohyb postavy
    stisknute_klavesy = pygame.key.get_pressed()
    if stisknute_klavesy[pygame.K_d]:  
        pozice_x_hrace += rychlost
    if stisknute_klavesy[pygame.K_a]:  
        pozice_x_hrace -= rychlost

    # Aplikace gravitace
    pozice_y_hrace += y_velocity
    y_velocity += gravitace

    # Kolidujeme se zemí
    if pozice_y_hrace >= zem:
        pozice_y_hrace = zem
        y_velocity = 0
        skace = False

    # Vykreslení
    screen.blit(background_image, (0, 0))
    screen.blit(postava, (pozice_x_hrace, pozice_y_hrace))

    pygame.display.update()
