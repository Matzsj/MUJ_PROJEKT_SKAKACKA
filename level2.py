import sys
import pygame
import time
import random

pygame.init() 

rozliseni_vyska = 600
rozliseni_sirka = 800




rect1 = pygame.Rect(50, 250, 200, 50)
rect2 = pygame.Rect(550, 250, 200, 50)
rect3 = pygame.Rect(296, 250, 200, 50)


posledni_kolize_cas = 0
nesmrtelnost_cas = 1000

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

cervena_zivot1 = (255, 0 , 0)
cervena_zivot2 = (255, 0 , 0)
cervena_zivot3 = (255, 0 , 0)

pygame.init()


pohyb_bossa = False
boss_smer = 3  # Počáteční směr pohybu (1 = doprava, -1 = doleva)


prekazky = [
    pygame.Rect(500, 363, 50, 50),
    ]


spiky = [
    [(550, 412), (599, 412), (573, 365)],
    ]

zivoty = [
    (40, 40, 15),  # (x, y, radius)
    (80, 40, 15),
    (120, 40, 15),
]


screen = pygame.display.set_mode((rozliseni_sirka, rozliseni_vyska))


clock = pygame.time.Clock()  # Inicializace hodin


while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
      
    screen.fill((0, 0, 0))
    
    # Kontrola stisknutých kláves
    klavesy = pygame.key.get_pressed()
    
    new_x_ctverec = x_ctverec
    new_y_ctverec = y_ctverec

    if klavesy[pygame.K_a]:  
        new_x_ctverec -= rychlost
    if klavesy[pygame.K_d]:  
        new_x_ctverec += rychlost
     
    posun_sveta = x_ctverec - rozliseni_sirka // 2 + 25  # Vypočítání posunu kamery
            
        # Skok
    if klavesy[pygame.K_SPACE] and not skace:  
        y_velocity = vyska_skoku  
        skace = True  
    
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


    def bod_v_trojuhelniku(bod, trojuhelnik):
        # Převede body na vektory
        A, B, C = map(pygame.math.Vector2, trojuhelnik)
        P = pygame.math.Vector2(bod)

        # Vypočítá plochu trojúhelníku pomocí determinantů
        def plocha(X, Y, Z):
            return abs((X.x * (Y.y - Z.y) + Y.x * (Z.y - X.y) + Z.x * (X.y - Y.y)) / 2.0)

        # Celková plocha trojúhelníku ABC
        plocha_ABC = plocha(A, B, C)

        # Plochy podtrojúhelníků APB, BPC, CPA
        plocha_ABP = plocha(A, B, P)
        plocha_BCP = plocha(B, C, P)
        plocha_CAP = plocha(C, A, P)

        # Pokud součet podtrojúhelníků odpovídá původní ploše, bod je uvnitř
        return abs(plocha_ABC - (plocha_ABP + plocha_BCP + plocha_CAP)) < 0.01
    
    je_v_kolizi = False  # Přidejte tuto proměnnou na začátek cyklu
    checkpoint_reached = False
    
    for spike in spiky:
        # Seznam bodů po obvodu postavy pro lepší detekci
        body_postavy = [
            (postava_rect.left + i, postava_rect.top + j) 
            for i in range(0, 51, 10)  # Vytvoří body podél šířky postavy
            for j in range(0, 51, 10)  # Vytvoří body podél výšky postavy
        ]

        for bod in body_postavy:
            if bod_v_trojuhelniku(bod, spike):
                aktualni_cas = pygame.time.get_ticks()

                # Zkontrolujte, zda je postava v kolizi a zda uplynul čas pro odebrání života
                if not je_v_kolizi and aktualni_cas - posledni_kolize_cas > nesmrtelnost_cas:
                    je_v_kolizi = True  # Nastavte, že postava je v kolizi
                    posledni_kolize_cas = aktualni_cas
                    
                    print("Kolize s bodcem!")  # Výpis ihned při detekci
                    if cervena_zivot3 == (255, 0, 0):
                        cervena_zivot3 = (0, 0, 0)
                        new_y_ctverec = 100
                        new_x_ctverec = 100
                     
                    elif cervena_zivot3 == (0, 0, 0) and cervena_zivot2 == (255, 0, 0):
                        cervena_zivot2 = (0, 0, 0)
                        cervena_zivot1 = (255, 0, 0)
                        new_y_ctverec = 100
                        new_x_ctverec = 100
                    else:
                        cervena_zivot1 = (0, 0, 0)
                        new_y_ctverec = 100
                        new_x_ctverec = 100   
    
    
    
       # Na konci herního cyklu resetujte stav kolize, pokud není postava v kolizi
    if not je_v_kolizi:
        je_v_kolizi = False


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
    

    
    # Postava
    pygame.draw.rect(screen, barva_ctverce, (x_ctverec - posun_sveta, y_ctverec + 2, 50, 51))
    pygame.draw.circle(screen, barva_ocí, (x_ctverec - posun_sveta + 15, y_ctverec + 15), 9.999)  
    pygame.draw.circle(screen, barva_zornic, (x_ctverec - posun_sveta + 15, y_ctverec + 15), 5)   
    pygame.draw.circle(screen, barva_ocí, (x_ctverec - posun_sveta + 35, y_ctverec + 15), 9.999)  
    pygame.draw.circle(screen, barva_zornic, (x_ctverec - posun_sveta + 35, y_ctverec + 15), 5)   

    # Překážky
    for prekazka in prekazky:
        pygame.draw.rect(screen, (0, 0, 255), (prekazka.x - posun_sveta, prekazka.y, prekazka.width, prekazka.height))  
    
    

    pygame.draw.circle(screen, cervena_zivot3, (40, 40), 15)
    pygame.draw.circle(screen, cervena_zivot2, (80, 40), 15)
    pygame.draw.circle(screen, cervena_zivot1, (120, 40), 15)
    
    
    
    
    for spike in spiky:
        posunuty_spike = [(x - posun_sveta, y) for x, y in spike]  # Posuneme každý bod zvlášť
        pygame.draw.polygon(screen, (127, 127, 127), posunuty_spike)
    
    font = pygame.font.Font(None, 50)  # None znamená výchozí font, 36 je velikost písma
    text = "level 2"  # Text, který chcete vykreslit
    text_surface = font.render(text, True, (0, 0, 0))  # Bílý text
    text_rect = text_surface.get_rect(center=(rozliseni_sirka // 2, 50))  # Umístění textu na obrazovku
    screen.blit(text_surface, text_rect)  # Vykreslení textu na obrazovku
     
    cerna = (0,0,0) 

    if cervena_zivot1 == (0,0,0) and cervena_zivot2 == (0,0,0) and cervena_zivot3 == (0,0,0):
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 255, 255), rect1, 2)
        pygame.draw.rect(screen, (255, 255, 255), rect2, 2)
        font = pygame.font.Font(None, 36)  # None znamená výchozí font, 36 je velikost písma
        text = "hrát znovu"  # Text, který chcete vykreslit
        text_surface = font.render(text, True, (255, 255, 255))  # Bílý text
        text_rect = text_surface.get_rect(center=(150, 275))  # Umístění textu na obrazovku
        screen.blit(text_surface, text_rect)  # Vykreslení textu na obrazovku
        font = pygame.font.Font(None, 36)  # None znamená výchozí font, 36 je velikost písma
        text = "ukončit hru"  # Text, který chcete vykreslit
        text_surface = font.render(text, True, (255, 255, 255))  # Bílý text
        text_rect = text_surface.get_rect(center=(655, 275))  # Umístění textu na obrazovku
        screen.blit(text_surface, text_rect)  # Vykreslení textu na obrazovku

    if udalost.type == pygame.MOUSEBUTTONDOWN:
            if rect1.collidepoint(udalost.pos):
                screen.blit(background_image, (0, 0)) # Změna barvy obdélníku 1
                new_y_ctverec = 100
                new_x_ctverec = 200
                cervena_zivot1 = (255, 0, 0)
                cervena_zivot2 = (255, 0, 0)
                cervena_zivot3 = (255, 0, 0)
                pohyb_bossa = False
            if rect2.collidepoint(udalost.pos):
                pygame.quit()
                sys.exit() 
    
    
    pygame.display.update()
    
    clock.tick(50) 