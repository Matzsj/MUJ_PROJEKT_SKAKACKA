import sys
import pygame 

# Inicializace Pygame
pygame.init() 

# Rozlišení okna
rozliseni_vyska = 600
rozliseni_sirka = 800

# Vlastnosti postavy
rychlost = 9
vyska_skoku = -14
gravitace = 1
y_velocity = 0
pozice_x_hrace = 100
pozice_y_hrace = 75
skace = False

clock = pygame.time.Clock()

#PREKAZKY
VYSKA_ZEM_PREKAZEK = 363

posun_sveta = 0



skok = 0


prekazky = [
    (20,VYSKA_ZEM_PREKAZEK, 50, 50), 
    (800, VYSKA_ZEM_PREKAZEK, 50, 50),
    (1200, VYSKA_ZEM_PREKAZEK, 50, 50),
    (1600, VYSKA_ZEM_PREKAZEK, 50, 50)
]


RED = (255, 0, 0)



# Vytvoření okna
screen = pygame.display.set_mode((rozliseni_sirka, rozliseni_vyska))
 
 # Načtení obrázk pozadí
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
        
    #Pohyb postavy
    stisknute_klavesy = pygame.key.get_pressed()
    if stisknute_klavesy[pygame.K_a]:
        posun_sveta += rychlost  # Posune svět doprava

    if stisknute_klavesy[pygame.K_d]:
        posun_sveta -= rychlost
    
    if stisknute_klavesy[pygame.K_SPACE]:
        skok += vyska_skoku
        
    if stisknute_klavesy[pygame.K_SPACE] and not skace:
        y_velocity = vyska_skoku
        skace = True
        
    pozice_y_hrace += y_velocity
    y_velocity += gravitace
    
    if pozice_y_hrace >= 75:
        pozice_y_hrace = 75
        y_velocity = 0
        skace = False 
    
    
    screen.blit(background_image, (0, 0))
        
    

    # Vykreslení
    for x, y, w, h in prekazky:
        pygame.draw.rect(screen, RED, (x + posun_sveta, y, w, h))
        
    screen.blit(postava, (pozice_x_hrace, pozice_y_hrace))

    pygame.display.update()
    
    

    clock.tick(60)
