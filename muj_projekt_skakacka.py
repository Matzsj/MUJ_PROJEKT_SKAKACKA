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
rychlost = 5.65  # Rychlost pohybu

gravitace = 1
y_velocity = 0 
vyska_skoku = - 12.6  # Skok

skace = False



<<<<<<< HEAD
pohybujici_prekazkax1 = 3200

=======


pohybujici_prekazkax1 = 3200
pohybujici_prekazkay1 = 300
>>>>>>> origin/main


screen = pygame.display.set_mode((rozliseni_sirka, rozliseni_vyska))

# Seznam překážek
prekazky = [
    pygame.Rect(500, 363, 50, 50),  # Překážka nižší než zem
    pygame.Rect(600, 343, 50, 70),   # Vyšší překážka
    pygame.Rect(780, 313, 250, 100),
    pygame.Rect(1120, 260, 70, 30),
    pygame.Rect(1290, 230, 70, 30),
    pygame.Rect(1460, 260, 70, 30),
    pygame.Rect(1630, 230, 70, 30),
    pygame.Rect(1800, 260, 70, 30),
    pygame.Rect(2000, 313, 250, 100),
    pygame.Rect(2620, 344, 60, 70),
    pygame.Rect(2720, 274, 60, 12),
    pygame.Rect(2544, 195, 60, 12),
    pygame.Rect(2718, 118, 62, 12),
    pygame.Rect(2770, 118, 60, 295),
    pygame.Rect(2830, 148, 70, 19),
    pygame.Rect(2900, 165, 70, 19),
    pygame.Rect(2970, 182, 70, 19),
    pygame.Rect(3040, 199, 70, 19),
    pygame.Rect(3110, 216, 70, 19),
<<<<<<< HEAD
    pygame.Rect(pohybujici_prekazkax1, 216, 70, 19),
=======
    pygame.Rect(3200, 216, 70, 19),
    pygame.Rect(3800, 216, 250, 197),
    pygame.Rect(4100, 160, 60, 19),
    pygame.Rect(4220, 340, 60, 19),
    pygame.Rect(4300, 300, 60, 19),
    pygame.Rect(4430, 300, 5, 20),
    pygame.Rect(4560, 300, 5, 20),
    pygame.Rect(4690, 300, 5, 20),
    pygame.Rect(4820, 300, 5, 20),
    pygame.Rect(4265, 300, 40, 59),
    pygame.Rect(4920, 300, 60, 20),
>>>>>>> origin/main
]



<<<<<<< HEAD




=======
posledni_prekazka = prekazky[19]
 


posledni_prekazkay = prekazky[29]

  # Pro ověření, že funguje správně


pohybujici_prekazka_smery = -2  # Začíná pohybem nahoru

>>>>>>> origin/main

# Načtení pozadí
try:
    background_image = pygame.image.load('backgroundColorForest.png')
    background_image = pygame.transform.scale(background_image, (rozliseni_sirka, rozliseni_vyska))
except pygame.error as e:
    print(f"Chyba při načítání obrázku: {e}")
    pygame.quit()
    sys.exit()

clock = pygame.time.Clock()  # Inicializace hodin

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

        # Ověření kolize X a Y zvlášť
    kolize_x = False
    kolize_y = False
    stoji_na_prekazce = False  

    for prekazka in prekazky:
        if postava_rect.colliderect(prekazka):
            # Kolize shora (dopad na překážku)
            if y_velocity > 0 and postava_rect.bottom > prekazka.top and postava_rect.bottom - y_velocity <= prekazka.top:
                if postava_rect.right > prekazka.left + 5 and postava_rect.left < prekazka.right - 5:
                    new_y_ctverec = prekazka.top - 50   # Opraveno na správnou výšku
                    y_velocity = 0
                    skace = False
                    kolize_y = True
                    stoji_na_prekazce = True  

            # Kolize zespodu (náraz hlavou)
            if y_velocity < 0 and postava_rect.top <= prekazka.bottom and postava_rect.bottom > prekazka.bottom:
                new_y_ctverec = prekazka.bottom
                y_velocity = 0
                kolize_y = True

            # Kolize z boku – ale dovolíme skok a pád dolů
            if postava_rect.right >= prekazka.left and postava_rect.left < prekazka.left and postava_rect.bottom > prekazka.top + 5:
                new_x_ctverec = prekazka.left - 50  
                kolize_x = True
            elif postava_rect.left <= prekazka.right and postava_rect.right > prekazka.right and postava_rect.bottom > prekazka.top + 5:
                new_x_ctverec = prekazka.right  
                kolize_x = True

                
<<<<<<< HEAD
            
=======
    # Změna směru pohybu
    pohyb_prekx = 2
    if pohybujici_prekazkax1 <= 3200:
        pohybujici_prekazka_smer = 2
    elif pohybujici_prekazkax1 >= 3700:
        pohybujici_prekazka_smer = -2

    # Posun překážky
    pohybujici_prekazkax1 += pohybujici_prekazka_smer

>>>>>>> origin/main

    # Aktualizace polohy pohybující se překážky v seznamu
    prekazky[19].x = pohybujici_prekazkax1
        
        
       # Změna směru pohybu
    pohyb_preky = 2
    if pohybujici_prekazkay1 >= 300:
        pohybujici_prekazka_smery = -2
    elif pohybujici_prekazkay1 <= 100:
        pohybujici_prekazka_smery = 2

    # Posun překážky
    pohybujici_prekazkay1 += pohybujici_prekazka_smery


    # Aktualizace polohy pohybující se překážky v seznamu
    prekazky[29].y = pohybujici_prekazkay1     


    if (
        postava_rect.bottom + y_velocity >= prekazky[29].top
        and postava_rect.bottom <= prekazky[29].top + abs(y_velocity) + 5  # Tolerance pro přesnost dopadu
        and postava_rect.right > prekazky[29].left + 5
        and postava_rect.left < prekazky[29].right - 5
    ):
        new_y_ctverec = prekazky[29].top - 50  # Umístění přesně na překážku
        y_velocity = pohybujici_prekazka_smery  # Pohyb spolu s překážkou
        skace = False

              
            
    def stoji_na_prekazce_funkce(postava_rect, prekazky, y_velocity):
        for prekazka in prekazky:
            if (
                2 + postava_rect.bottom + y_velocity >= prekazka.top and  # Postava je těsně nad překážkou
                postava_rect.bottom <= prekazka.top + 5 and  # Tolerance pro přesnost dopadu
                postava_rect.right > prekazka.left + 5 and  # Část postavy je na překážce
                postava_rect.left < prekazka.right - 5
            ):
                return True
        return False
    
    # Změna směru pohybu
    pohyb_prekx = 2
    if pohybujici_prekazkax1 <= 3200:
        pohybujici_prekazka_smer = 2
    elif pohybujici_prekazkax1 >= 3700:
        pohybujici_prekazka_smer = -2

    # Posun překážky
    pohybujici_prekazkax1 += pohybujici_prekazka_smer

    
    # Aktualizace polohy pohybující se překážky v seznamu
    prekazky[19].x = pohybujici_prekazkax1

        
    
    
    stoji_na_prekazce = stoji_na_prekazce_funkce(postava_rect, prekazky, y_velocity)

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
    posun_sveta = x_ctverec - rozliseni_sirka // 2 + 25  # Vypočítání posunu kamery

    # Kreslení
    screen.blit(background_image, (0, 0))

    # Postava
    pygame.draw.rect(screen, barva_ctverce, (x_ctverec - posun_sveta, y_ctverec + 2, 50, 51))
    pygame.draw.circle(screen, barva_ocí, (x_ctverec - posun_sveta + 15, y_ctverec + 15), 9.999)  
    pygame.draw.circle(screen, barva_zornic, (x_ctverec - posun_sveta + 15, y_ctverec + 15), 5)   
    pygame.draw.circle(screen, barva_ocí, (x_ctverec - posun_sveta + 35, y_ctverec + 15), 9.999)  
    pygame.draw.circle(screen, barva_zornic, (x_ctverec - posun_sveta + 35, y_ctverec + 15), 5)   

    # Překážky
    for prekazka in prekazky:
        pygame.draw.rect(screen, (0, 0, 255), (prekazka.x - posun_sveta, prekazka.y, prekazka.width, prekazka.height))  
    
    pygame.draw.rect(screen, (0, 255, 0), (posledni_prekazka.x - posun_sveta, posledni_prekazka.y, posledni_prekazka.width, posledni_prekazka.height))
    pygame.draw.rect(screen, (0, 255, 0), (posledni_prekazkay.x, posledni_prekazkay.y, posledni_prekazkay.width, posledni_prekazkay.height))
    
    font = pygame.font.Font(None, 50)  # None znamená výchozí font, 36 je velikost písma
    text = "level 1"  # Text, který chcete vykreslit
    text_surface = font.render(text, True, (0, 0, 0))  # Bílý text
    text_rect = text_surface.get_rect(center=(rozliseni_sirka // 2, 50))  # Umístění textu na obrazovku
    screen.blit(text_surface, text_rect)  # Vykreslení textu na obrazovku
        
    pygame.display.update()
    
    clock.tick(60) 