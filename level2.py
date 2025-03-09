import sys
import pygame
import time
import random
import subprocess

pygame.init() 

rozliseni_vyska = 600
rozliseni_sirka = 800




rect1 = pygame.Rect(50, 250, 200, 50)
rect2 = pygame.Rect(550, 250, 200, 50)
rect3 = pygame.Rect(296, 250, 200, 50)


posledni_kolize_cas = 0
nesmrtelnost_cas = 1000

barva_ctverce = (255, 0, 0)  
barva_ocí = (255, 255, 255)   
barva_zornic = (0, 0, 0)      

# Počáteční pozice čtverce
x_ctverec = rozliseni_sirka // 2 - 25 
y_ctverec = 344 
rychlost = 30
#5.65 


gravitace = 1
y_velocity = 0 
vyska_skoku = - 30
#- 12.6  # Skok

skace = False

cervena_zivot1 = (255, 0 , 0)
cervena_zivot2 = (255, 0 , 0)
cervena_zivot3 = (255, 0 , 0)

pygame.init()



pohyb_bossa = False
boss_smer = 3  # Počáteční směr pohybu (1 = doprava, -1 = doleva)


prekazky = [
    pygame.Rect(0, 347, 50, 50),
    pygame.Rect(-100, 290, 50, 107),
    pygame.Rect(-200, 233, 50, 107),
    pygame.Rect(-300, 176, 50, 107),
    pygame.Rect(-210, 85, 1500, 8),
    pygame.Rect(2200, 310, 1500, 90),
    pygame.Rect(2200, 105, 140, 140),
    pygame.Rect(2200, 0, 1500, 100),
    pygame.Rect(2100, 325, 50, 72),
    pygame.Rect(2200, 250, 200, 107),
    pygame.Rect(2460, 250, 350, 107),
    pygame.Rect(2870, 250, 350, 107),
    pygame.Rect(3280, 250, 420, 107),
    pygame.Rect(3850, 250, 70, 20),
    pygame.Rect(4000, 250, 7, 147),
    pygame.Rect(4150, 250, 7, 147),
    pygame.Rect(4300, 250, 7, 147),
    pygame.Rect(4450, 250, 7, 147),
    pygame.Rect(4600, 250, 7, 147),
    pygame.Rect(4750, 250, 7, 147),
    pygame.Rect(4900, 250, 7, 147),
    pygame.Rect(5050, 250, 80, 148),
    pygame.Rect(5050, 0, 80, 190),
    pygame.Rect(5190, 280, 70, 7),
    pygame.Rect(5190, 250, 7, 30),
    pygame.Rect(5253, 250, 7, 30),
    pygame.Rect(5330, 280, 70, 7),
    pygame.Rect(5330, 250, 7, 30),
    pygame.Rect(5393, 250, 7, 30),
    pygame.Rect(5470, 280, 70, 7),
    pygame.Rect(5470, 250, 7, 30),
    pygame.Rect(5533, 250, 7, 30),
    pygame.Rect(5610, 280, 70, 7),
    pygame.Rect(5610, 250, 7, 30),
    pygame.Rect(5673, 250, 7, 30),
    pygame.Rect(5750, 280, 70, 7),
    pygame.Rect(5750, 250, 7, 30),
    pygame.Rect(5813, 250, 7, 30),
    pygame.Rect(5890, 280, 70, 7),
    pygame.Rect(5890, 250, 7, 30),
    pygame.Rect(5953, 250, 7, 30),
    pygame.Rect(6100, 0, 700, 300),
    pygame.Rect(7300, 0, 100, 200),
    pygame.Rect(7500, 0, 100, 200),
    pygame.Rect(7700, 0, 100, 200),
    pygame.Rect(7900, 0, 100, 200),
    pygame.Rect(8100, 0, 100, 200),
    pygame.Rect(8300, 0, 100, 200),
    pygame.Rect(8700, 337, 40, 60),
    pygame.Rect(8800, 277, 40, 120),
    pygame.Rect(8900, 217, 40, 180),
    pygame.Rect(9000, 157, 40, 240),
    pygame.Rect(9150, 157, 200, 240),
    pygame.Rect(9400, 157, 70, 20),
    pygame.Rect(10450, 157, 70, 20),
    pygame.Rect(10570, 157, 70, 20),
    pygame.Rect(11050, 157, 200, 240),
    pygame.Rect(11500, 347, 120, 50),
    pygame.Rect(11740, 347, 120, 50),
    pygame.Rect(11980, 347, 120, 50),
    pygame.Rect(12220, 347, 120, 50),
    pygame.Rect(12460, 347, 120, 50),
    pygame.Rect(12800, 307, 70, 20),
    pygame.Rect(12940, 267, 70, 20),
    pygame.Rect(13080, 227, 70, 20),
    pygame.Rect(13220, 187, 70, 20),
    pygame.Rect(13360, 147, 70, 20),
    pygame.Rect(13500, 147, 200, 250),
    pygame.Rect(15000, 0, 500, 397),
    pygame.Rect(14900, 392, 100, 5),
    pygame.Rect(14900, 327, 5, 65),
    ]


spiky = [
    [(550, 396), (599, 396), (573, 349)],
    ]

zivoty = [
    (40, 40, 15),  # (x, y, radius)
    (80, 40, 15),
    (120, 40, 15),
]

pohybujici_prekazkax1 = 2200

screen = pygame.display.set_mode((rozliseni_sirka, rozliseni_vyska))


# Načtení pozadí
try:
    background_image = pygame.image.load('level2_background.png').convert()
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
      
    screen.blit(background_image, (0, 0))
    
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


    # Indexy překážek, které se budou pohybovat
    pohyblive_prekazky = [42, 43, 44, 45, 46, 47, 48]
    pohyblive_prekazky2 = [6, 42, 43, 44, 45, 46, 47, 48]
    

    # Počáteční hodnoty Y pro každou překážku (musí být definovány mimo hlavní smyčku hry!)
    if 'pohyblive_y' not in globals():
        pohyblive_y = {i: prekazky[i].y for i in pohyblive_prekazky}
        pohyblive_smery = {i: 2 for i in pohyblive_prekazky}  # Všechno začne pohybem dolů

    # Logika pohybu pro každou překážku
    for i in pohyblive_prekazky:
        if pohyblive_y[i] >= 200:
            pohyblive_smery[i] = -2
        elif pohyblive_y[i] <= 0:
            pohyblive_smery[i] = 2

        pohyblive_y[i] += pohyblive_smery[i]
        prekazky[i].y = pohyblive_y[i]



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
    if not kolize_y and not stoji_na_prekazce and new_y_ctverec >= 344:  
        new_y_ctverec = 344
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

    barva = (80, 80, 80)

    for i, prekazka in enumerate(prekazky):
        if i in [6, 42, 43, 44, 45, 46, 47, 48]:  # Změní barvu jen u vybraných překážek
            barva = (255, 0, 0)  # Červená
        else:
            barva = (80, 80, 80)  # Šedá
        
        pygame.draw.rect(screen, barva, (prekazka.x - posun_sveta, prekazka.y, prekazka.width, prekazka.height))


        

    pygame.draw.circle(screen, cervena_zivot3, (40, 40), 15)
    pygame.draw.circle(screen, cervena_zivot2, (80, 40), 15)
    pygame.draw.circle(screen, cervena_zivot1, (120, 40), 15)
    
    pohyb_prekx = 2
    if pohybujici_prekazkax1 <= 2200:
        pohybujici_prekazka_smer = 4
    elif pohybujici_prekazkax1 >= 3560:
        pohybujici_prekazka_smer = -4
        
    

    # Posun překážky
    pohybujici_prekazkax1 += pohybujici_prekazka_smer


    # Aktualizace polohy pohybující se překážky v seznamu
    prekazky[6].x = pohybujici_prekazkax1
    
    
    
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
        new_y_ctverec = 100
        new_x_ctverec = 200
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
            pygame.quit()
            subprocess.run(["python", "level2.py"])
            sys.exit()


        if rect2.collidepoint(udalost.pos):
            pygame.quit()
            sys.exit() 

    for i in pohyblive_prekazky2:
        if postava_rect.colliderect(prekazky[i]):
            print("Kolize s překážkou!", i)  

            # Ztráta životů
            cervena_zivot3 = (0, 0, 0)
            cervena_zivot2 = (0, 0, 0)
            cervena_zivot1 = (0, 0, 0)


                        
          
    
    pygame.display.update()
    
    clock.tick(50) 