import sys
import pygame 

pygame.init() 

rozliseni_vyska = 600
rozliseni_sirka = 800

barva_ctverce = (255, 0, 0)  # Červená barva pro čtverec
barva_ocí = (255, 255, 255)   # Bílá barva pro oči
barva_zornic = (0, 0, 0)      # Černá barva pro zornice

# Počáteční pozice čtverce
x_ctverec = rozliseni_sirka // 2 - 25  # Střed čtverce
y_ctverec = 363  # Počáteční výška na zemi
rychlost = 5  # Rychlost pohybu

gravitace = 1
y_velocity = 0 
vyska_skoku = -15  # Skok

skace = False

screen = pygame.display.set_mode((rozliseni_sirka, rozliseni_vyska))

# Seznam překážek
prekazky = [
    pygame.Rect(500, 363, 50, 50),  # Překážka nižší než zem
    pygame.Rect(650, 363, 50, 50)   # Vyšší překážka
]

# Načtení pozadí
try:
    background_image = pygame.image.load('backgroundColorForest.png')
    background_image = pygame.transform.scale(background_image, (rozliseni_sirka, rozliseni_vyska))
except pygame.error as e:
    print(f"Chyba při načítání obrázku: {e}")
    pygame.quit()
    sys.exit()

clock = pygame.time.Clock()  # Inicializace hodin

# Proměnná pro pozici kamery
camera_x = 0

while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()   

    # Kontrola stisknutých kláves
    klavesy = pygame.key.get_pressed()
    
    new_x_ctverec = x_ctverec
    new_y_ctverec = y_ctverec

    if klavesy[pygame.K_a]:  
        new_x_ctverec -= rychlost
    if klavesy[pygame.K_d]:  
        new_x_ctverec += rychlost
        
    # Skok
    if klavesy[pygame.K_SPACE] and not skace:  
        y_velocity = vyska_skoku  
        skace = True  

    # Gravitace
    new_y_ctverec += y_velocity  
    y_velocity += gravitace  

    # Vytvoření Rect objektu pro postavu
    postava_rect = pygame.Rect(new_x_ctverec, new_y_ctverec, 50, 50)

    # Ověření kolize
    kolize_x = False
    kolize_y = False
    stoji_na_prekazce = False  # Přidáno pro kontrolu, zda postava stojí na překážce
    for prekazka in prekazky:
        if postava_rect.colliderect(prekazka):
            # Kolize shora (dopad na překážku)
            if y_velocity > 0 and postava_rect.bottom > prekazka.top and postava_rect.bottom - y_velocity <= prekazka.top:
                if postava_rect.right > prekazka.left + 20 and postava_rect.left < prekazka.right - 20:
                    new_y_ctverec = prekazka.top - 50  
                    y_velocity = 0
                    skace = False
                    kolize_y = True
                    stoji_na_prekazce = True  # Nastavíme, že stojí na překážce

            # Kolize zespodu (náraz hlavou)
            if y_velocity > 0 and postava_rect.bottom >= prekazka.top and postava_rect.top < prekazka.top:
                new_y_ctverec = prekazka.bottom
                y_velocity = 0
                kolize_y = True

            # Kolize z boku
            if postava_rect.right >= prekazka.left and postava_rect.left < prekazka.left:
                new_x_ctverec = prekazka.left - 50  
                kolize_x = True
            elif postava_rect.left <= prekazka.right and postava_rect.right > prekazka.right:
                new_x_ctverec = prekazka.right  
                kolize_x = True

    stoji_na_prekazce = any(
        postava_rect.bottom >= prekazka.top and
        postava_rect.bottom - y_velocity <= prekazka.top and
        postava_rect.right > prekazka.left + 20 and
        postava_rect.left < prekazka.right - 20
        for prekazka in prekazky
    )

    if stoji_na_prekazce:
        y_velocity = 0
        skace = False

    # Ověření, zda postava stojí na zemi
    if not kolize_y and not stoji_na_prekazce and new_y_ctverec >= 363:  
        new_y_ctverec = 363
        y_velocity = 0
        skace = False

    # Aktualizace pozice
    x_ctverec = new_x_ctverec
    y_ctverec = new_y_ctverec

    # Posun kamery
    camera_x = x_ctverec - rozliseni_sirka // 2 + 25  # Posun kamery podle pozice postavy

    # Kreslení
    screen.blit(background_image, (0, 0))

    # Vykreslení postavy a překážek
    pygame.draw.rect(screen, barva_ctverce, (x_ctverec - camera_x, y_ctverec + 2, 50, 51))
    pygame.draw.circle(screen, barva_ocí, (x_ctverec - camera_x + 15, y_ctverec + 15), 10)  
    pygame.draw.circle(screen, barva_zornic, (x_ctverec - camera_x + 15, y_ctverec + 15), 5)   
    pygame.draw.circle(screen, barva_ocí, (x_ctverec - camera_x + 35, y_ctverec + 15), 10)  
    pygame.draw.circle(screen, barva_zornic, (x_ctverec - camera_x + 35, y_ctverec + 15), 5)   

    # Překážky
    for prekazka in prekazky:
        pygame.draw.rect(screen, (0, 0, 255), (prekazka.x - camera_x, prekazka.y, prekazka.width, prekazka.height))  

    pygame.display.update()
    
    clock.tick(60)
