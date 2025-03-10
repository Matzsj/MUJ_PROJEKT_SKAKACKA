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
rychlost = 25
#6


gravitace = 1
y_velocity = 0 
vyska_skoku = -60
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
    pygame.Rect(10980, 157, 70, 20),
    
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

[(542, 396), (591, 396), (566, 349)],
[(598, 396), (647, 396), (622, 349)],
[(654, 396), (703, 396), (678, 349)],
[(710, 396), (759, 396), (734, 349)],
[(766, 396), (815, 396), (790, 349)],
[(822, 396), (871, 396), (846, 349)],
[(878, 396), (927, 396), (902, 349)],
[(934, 396), (983, 396), (958, 349)],
[(990, 396), (1039, 396), (1014, 349)],
[(1046, 396), (1095, 396), (1070, 349)],
[(1102, 396), (1151, 396), (1126, 349)],
[(1158, 396), (1207, 396), (1182, 349)],
[(1214, 396), (1263, 396), (1238, 349)],
[(1270, 396), (1319, 396), (1294, 349)],
[(1326, 396), (1375, 396), (1350, 349)],
[(1382, 396), (1431, 396), (1406, 349)],

[(1560, 396), (1589, 396), (1574, 349)],

[(1672, 396), (1701, 396), (1686, 349)],

[(1784, 396), (1813, 396), (1798, 349)],

[(1896, 396), (1925, 396), (1910, 349)],








[(3734, 396), (3783, 396), (3758, 349)],
[(3790, 396), (3839, 396), (3814, 349)],
[(3846, 396), (3895, 396), (3870, 349)],
[(3902, 396), (3951, 396), (3926, 349)],
[(3958, 396), (4007, 396), (3982, 349)],
[(4014, 396), (4063, 396), (4038, 349)],
[(4070, 396), (4119, 396), (4094, 349)],
[(4126, 396), (4175, 396), (4150, 349)],
[(4182, 396), (4231, 396), (4206, 349)],
[(4238, 396), (4287, 396), (4262, 349)],
[(4294, 396), (4343, 396), (4318, 349)],
[(4350, 396), (4399, 396), (4374, 349)],
[(4406, 396), (4455, 396), (4430, 349)],
[(4462, 396), (4511, 396), (4486, 349)],
[(4518, 396), (4567, 396), (4542, 349)],
[(4574, 396), (4623, 396), (4598, 349)],
[(4630, 396), (4679, 396), (4654, 349)],
[(4686, 396), (4735, 396), (4710, 349)],
[(4742, 396), (4791, 396), (4766, 349)],
[(4798, 396), (4847, 396), (4822, 349)],
[(4854, 396), (4903, 396), (4878, 349)],
[(4910, 396), (4959, 396), (4934, 349)],
[(4910, 396), (4959, 396), (4934, 349)],
[(4966, 396), (5015, 396), (4990, 349)],

[(5134, 396), (5183, 396), (5158, 349)],
[(5190, 396), (5239, 396), (5214, 349)],
[(5246, 396), (5295, 396), (5270, 349)],
[(5302, 396), (5351, 396), (5326, 349)],
[(5358, 396), (5407, 396), (5382, 349)],
[(5414, 396), (5463, 396), (5438, 349)],
[(5470, 396), (5519, 396), (5494, 349)],
[(5526, 396), (5575, 396), (5550, 349)],
[(5582, 396), (5631, 396), (5606, 349)],
[(5638, 396), (5687, 396), (5662, 349)],
[(5694, 396), (5743, 396), (5718, 349)],
[(5750, 396), (5799, 396), (5774, 349)],
[(5806, 396), (5855, 396), (5830, 349)],
[(5862, 396), (5911, 396), (5886, 349)],
[(5916, 396), (5965, 396), (5940, 349)],
[(5972, 396), (6021, 396), (5996, 349)],

[(8746, 396), (8795, 396), (8770, 349)],

[(8848, 396), (8897, 396), (8872, 349)],

[(8944, 396), (8993, 396), (8968, 349)],


[(9039, 396), (9088, 396), (9063, 349)],
[(9097, 396), (9146, 396), (9121, 349)],



    
    ]

zivoty = [
    (40, 40, 15),  # (x, y, radius)
    (80, 40, 15),
    (120, 40, 15),
]

pohybujici_prekazkax1 = 2200

pohybujici_prekazkax2 = 9400

pohybujici_prekazkax3 = 10980



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
    pohyblive_prekazky = [42, 43, 44, 45, 46, 47, ]
    pohyblive_prekazky2 = [6, 42, 43, 44, 45, 46, 47, ]
    

    # Počáteční hodnoty Y pro každou překážku (musí být definovány mimo hlavní smyčku hry!)
    if 'pohyblive_y' not in globals():
        pohyblive_y = {i: prekazky[i].y for i in pohyblive_prekazky}
        pohyblive_smery = {i: 2 for i in pohyblive_prekazky}  # Všechno začne pohybem dolů

    # Logika pohybu pro každou překážku
    for i in pohyblive_prekazky:
        if pohyblive_y[i] >= 200:
            pohyblive_smery[i] = -5
        elif pohyblive_y[i] <= 0:
            pohyblive_smery[i] = 5

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
        if i in [6, 42, 43, 44, 45, 46, 47,]:  # Změní barvu jen u vybraných překážek
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
    
        
    
    pohyb_prekx = 2
    if pohybujici_prekazkax2 <= 9400:
        pohybujici_prekazka_smer1 = 4
    elif pohybujici_prekazkax2 >= 10145:
        pohybujici_prekazka_smer1 = -4
        
    

    # Posun překážky
    pohybujici_prekazkax2 += pohybujici_prekazka_smer1


    # Aktualizace polohy pohybující se překážky v seznamu
    prekazky[-17].x = pohybujici_prekazkax2
    
        
    pohyb_prekx = 2
    if pohybujici_prekazkax3 <= 10235:
        pohybujici_prekazka_smer2 = 4
    elif pohybujici_prekazkax3 >= 10980:
        pohybujici_prekazka_smer2 = -4
        
    

    # Posun překážky
    pohybujici_prekazkax3 += pohybujici_prekazka_smer2


    # Aktualizace polohy pohybující se překážky v seznamu
    prekazky[-16].x = pohybujici_prekazkax3
    
    
            

    
    

    
    
    
    
    
    
    
    
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
    
    clock.tick(60) 