import sys
import pygame 


pygame.init() 


rozliseni_vyska = 600
rozliseni_sirka = 800


screen = pygame.display.set_mode((rozliseni_sirka, rozliseni_vyska))


try:
    background_image = pygame.image.load('backgroundColorForest.png')
    background_image = pygame.transform.scale(background_image, (rozliseni_sirka, rozliseni_vyska))
except pygame.error as e:
    print(f"Chyba při načítání obrázku: {e}")
    pygame.quit()
    sys.exit()


# Načtení obrázku postavy PŘED hlavní smyčkou
try:
    postava = pygame.image.load('ufo-removebg-preview.png').convert_alpha()
except pygame.error as e:
    print(f"Chyba při načítání obrázku postavy: {e}")
    pygame.quit()
    sys.exit()


while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()   

    screen.blit(background_image, (0, 0))

    
    screen.blit(postava, (100, 90))  # Souřadnice X=100, Y=100

   
    
    
    

    
    pygame.display.update()
