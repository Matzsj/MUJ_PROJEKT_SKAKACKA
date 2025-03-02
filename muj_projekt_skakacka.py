import sys
import pygame
import time
import random

pygame.init() 

rozliseni_vyska = 600
rozliseni_sirka = 800


boss_timer = None

posledni_kolize_cas = 0
nesmrtelnost_cas = 1000


zobraz_text = True


rect1 = pygame.Rect(120, 250, 200, 50)
rect2 = pygame.Rect(500, 250, 200, 50)

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



pohybujici_prekazkax1 = 3200
pohybujici_prekazkay1 = 300


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
    pygame.Rect(5100, 100, 250, 314),
    pygame.Rect(5550, 300, 1100, 115),
    pygame.Rect(5550, 0, 1100, 150),
    pygame.Rect(6700, 300, 70, 20),
    pygame.Rect(6850, 300, 70, 20),
    pygame.Rect(7000, 300, 70, 20),
    pygame.Rect(7150, 300, 70, 20),
    pygame.Rect(7300, 300, 70, 20),
    pygame.Rect(7450, 300, 70, 20),
    pygame.Rect(7600, 300, 70, 20),
    pygame.Rect(7770, 394, 70, 20),
    pygame.Rect(7750, 314, 20, 100),
    pygame.Rect(7840, 0, 500, 414),
    pygame.Rect(9100, 0, 500, 414),
    pygame.Rect(10500, 0, 500, 414),
    pygame.Rect(9600, 313, 1000, 20),
    pygame.Rect(9720, 313, 70, 20),
    pygame.Rect(9840, 313, 70, 20),
    pygame.Rect(9960, 313, 100, 20),
    pygame.Rect(10080, 313, 70, 20),
    pygame.Rect(10200, 313, 70, 20),
    pygame.Rect(10320, 313, 70, 20),
    pygame.Rect(10440, 313, 130, 20),
]

zivoty = [
    (40, 40, 15),  # (x, y, radius)
    (80, 40, 15),
    (120, 40, 15),
]



spiky = [
    [(550, 412), (599, 412), (573, 365)],  
    [(650, 412), (688, 412), (669, 365)],  
    [(695, 412), (733, 412), (714, 365)],  # 
    [(740, 412), (778, 412), (759, 365)],  # Trojúhelník 2
    [(1035, 412), (1087, 412), (1060, 365)],  # Trojúhelník 1
    [(1087, 412), (1137, 412), (1110, 365)],  # Trojúhelník 2
    [(1137, 412), (1187, 412), (1160, 365)],  # Trojúhelník 3
    [(1187, 412), (1237, 412), (1210, 365)],  # Trojúhelník 4
    [(1237, 412), (1287, 412), (1260, 365)],  # Trojúhelník 5
    [(1287, 412), (1337, 412), (1310, 365)],  # Trojúhelník 6
    [(1337, 412), (1387, 412), (1360, 365)],  # Trojúhelník 7
    [(1387, 412), (1437, 412), (1410, 365)],  # Trojúhelník 8
    [(1437, 412), (1487, 412), (1460, 365)],  # Trojúhelník 9
    [(1487, 412), (1537, 412), (1510, 365)],  # Trojúhelník 10
    [(1537, 412), (1587, 412), (1560, 365)],  # Trojúhelník 11
    [(1587, 412), (1637, 412), (1610, 365)],  # Trojúhelník 12
    [(1637, 412), (1687, 412), (1660, 365)],  # Trojúhelník 13
    [(1687, 412), (1737, 412), (1710, 365)],  # Trojúhelník 14
    [(1737, 412), (1787, 412), (1760, 365)],  # Trojúhelník 15
    [(1787, 412), (1837, 412), (1810, 365)],  # Trojúhelník 16
    [(1837, 412), (1887, 412), (1860, 365)],  # Trojúhelník 17
    [(1887, 412), (1937, 412), (1910, 365)],  # Trojúhelník 18
    [(1937, 412), (1987, 412), (1960, 365)],
    [(2250, 412), (2300, 412), (2275, 365)],  # Trojúhelník 1
    [(2305, 412), (2355, 412), (2330, 365)],  # Trojúhelník 1
    [(2685, 412), (2735, 412), (2710, 365)],
    [(2830, 412), (2880, 412), (2855, 365)],  # Trojúhelník 1
    [(2905, 412), (2955, 412), (2930, 365)],  # Trojúhelník 2
    [(2970, 412), (3020, 412), (2995, 365)],  # Trojúhelník 3
    [(3035, 412), (3085, 412), (3060, 365)],  # Trojúhelník 4
    [(3100, 412), (3150, 412), (3125, 365)],  # Trojúhelník 5
    [(3165, 412), (3215, 412), (3190, 365)],  # Trojúhelník 6
    [(3230, 412), (3280, 412), (3255, 365)],  # Trojúhelník 7
    [(3295, 412), (3345, 412), (3320, 365)],  # Trojúhelník 8
    [(3360, 412), (3410, 412), (3385, 365)],  # Trojúhelník 9
    [(3425, 412), (3475, 412), (3450, 365)],  # Trojúhelník 10
    [(3490, 412), (3540, 412), (3515, 365)],  # Trojúhelník 11
    [(3555, 412), (3605, 412), (3580, 365)],  # Trojúhelník 12
    [(3620, 412), (3670, 412), (3645, 365)],  # Trojúhelník 13
    [(3685, 412), (3735, 412), (3710, 365)],  # Trojúhelník 14
    [(3750, 412), (3800, 412), (3775, 365)],
    [(4050, 412), (4100, 412), (4075, 365)],  # Trojúhelník 1
    [(4115, 412), (4165, 412), (4140, 365)],  # Trojúhelník 2
    [(4170, 412), (4220, 412), (4195, 365)],  # Trojúhelník 3
    [(4235, 412), (4285, 412), (4260, 365)],  # Trojúhelník 4
    [(4295, 412), (4345, 412), (4320, 365)],  # Trojúhelník 5
    [(4355, 412), (4405, 412), (4380, 365)],  # Trojúhelník 6
    [(4415, 412), (4465, 412), (4440, 365)],  # Trojúhelník 7
    [(4475, 412), (4525, 412), (4500, 365)],  # Trojúhelník 8
    [(4535, 412), (4585, 412), (4560, 365)],  # Trojúhelník 9
    [(4595, 412), (4645, 412), (4620, 365)],  # Trojúhelník 10
    [(4655, 412), (4705, 412), (4680, 365)],  # Trojúhelník 11
    [(4715, 412), (4765, 412), (4740, 365)],  # Trojúhelník 12
    [(4775, 412), (4825, 412), (4800, 365)],  # Trojúhelník 13
    [(4835, 412), (4885, 412), (4860, 365)],  # Trojúhelník 14
    [(4895, 412), (4945, 412), (4920, 365)],  # Trojúhelník 15
    [(4955, 412), (5005, 412), (4980, 365)],  # Trojúhelník 16
    [(5015, 412), (5065, 412), (5040, 365)],
    [(5350, 412), (5400, 412), (5375, 365)],  # Trojúhelník 1
    [(5350, 412), (5400, 412), (5375, 365)],  # Trojúhelník 1
    [(5400, 412), (5450, 412), (5425, 365)],  # Trojúhelník 2
    [(5450, 412), (5500, 412), (5475, 365)],
    [(5500, 412), (5550, 412), (5525, 365)],
    [(5600, 300), (5640, 300), (5620, 265)],  # Trojúhelník 1 (dole)
    [(5700, 150), (5740, 150), (5720, 180)],  # Trojúhelník 2 (nahoře, hrot dolů)
    [(5800, 300), (5840, 300), (5820, 265)],  # Trojúhelník 3 (dole)
    [(5900, 150), (5940, 150), (5920, 180)],  # Trojúhelník 4 (nahoře, hrot dolů)
    [(6000, 300), (6040, 300), (6020, 265)],  # Trojúhelník 5 (dole)
    [(6100, 150), (6140, 150), (6120, 180)],  # Trojúhelník 6 (nahoře, hrot dolů)
    [(6200, 300), (6240, 300), (6220, 265)],  # Trojúhelník 7 (dole)
    [(6300, 150), (6340, 150), (6320, 180)],  # Trojúhelník 8 (nahoře, hrot dolů)
    [(6400, 300), (6440, 300), (6420, 265)],  # Trojúhelník 9 (dole)
    [(6500, 150), (6540, 150), (6520, 180)],
    [(6650, 412), (6700, 412), (6675, 365)],  # Trojúhelník 1 (dole)
    [(6750, 412), (6800, 412), (6775, 365)],  # Trojúhelník 2 (dole)
    [(6850, 412), (6900, 412), (6875, 365)],  # Trojúhelník 3 (dole)
    [(6950, 412), (7000, 412), (6975, 365)],  # Trojúhelník 4 (dole)
    [(7050, 412), (7100, 412), (7075, 365)],  # Trojúhelník 5 (dole)
    [(7150, 412), (7200, 412), (7175, 365)],  # Trojúhelník 6 (dole)
    [(7250, 412), (7300, 412), (7275, 365)],  # Trojúhelník 7 (dole)
    [(7350, 412), (7400, 412), (7375, 365)],  # Trojúhelník 8 (dole)
    [(7450, 412), (7500, 412), (7475, 365)],  # Trojúhelník 9 (dole)
    [(7550, 412), (7600, 412), (7575, 365)],  # Trojúhelník 10 (dole)
    [(7650, 412), (7700, 412), (7675, 365)],
    [(9600, 412), (9648, 412), (9624, 365)],
    [(9648, 412), (9696, 412), (9672, 365)],
    [(9696, 412), (9744, 412), (9720, 365)],
    [(9744, 412), (9792, 412), (9768, 365)],
    [(9792, 412), (9840, 412), (9816, 365)],
    [(9840, 412), (9888, 412), (9864, 365)],
    [(9888, 412), (9936, 412), (9912, 365)],
    [(9936, 412), (9984, 412), (9960, 365)],
    [(9984, 412), (10032, 412), (10008, 365)],
    [(10032, 412), (10080, 412), (10056, 365)],
    [(10080, 412), (10128, 412), (10104, 365)],
    [(10128, 412), (10176, 412), (10152, 365)],
    [(10176, 412), (10224, 412), (10200, 365)],
    [(10224, 412), (10272, 412), (10248, 365)],
    [(10272, 412), (10320, 412), (10296, 365)],
    [(10320, 412), (10368, 412), (10344, 365)],
    [(10368, 412), (10416, 412), (10392, 365)],
    [(10416, 412), (10464, 412), (10440, 365)],
]



posledni_prekazka = prekazky[19]
 

bossx = 9600
bossy = 260
boss_smer = 1  # Počáteční směr pohybu (1 znamená, že se pohybuje doprava)
speed = 2


posledni_prekazkay = prekazky[29]

  # Pro ověření, že funguje správně


pohybujici_prekazka_smery = -2  # Začíná pohybem nahoru


# Načtení pozadí
try:
    background_image = pygame.image.load('backgroundColorForest.png').convert()
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
    
    
    # Kreslení
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

    

    # Kontrola stisknutí klávesy 'L'
    if klavesy[pygame.K_l] and zobraz_text:
        pohyb_bossa = True  # Spusť pohyb, pokud je stisknuta klávesa 'L'
        zobraz_text = False
    # Pokud je pohyb spuštěn, posuň překážku
    if pohyb_bossa:
        bossx += speed * boss_smer
        textl = ' '
        # Změna směru při dosažení hranic
        if bossx <= 9620:  # Při dosažení levé hranice
            boss_smer = 1  # Změň směr na doprava
        elif bossx >= 10380:  # Při dosažení pravé hranice
            boss_smer = -1  # Změň směr na doleva

    if zobraz_text:
        font = pygame.font.Font(None, 50)  # None znamená výchozí font, 36 je velikost písma
        textl = "zmáčkni L abys začal boss fight"  # Text, který chcete vykreslit
        text_surface = font.render(textl, True, (0, 0, 0))  # Bílý text
        text_rect = text_surface.get_rect(center=(10000 - posun_sveta, 200))  # Umístění textu na obrazovku
        screen.blit(text_surface, text_rect)  # Vykreslení textu na obrazovku

    
     
     
     
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
                        if len(prekazky) > 30:
                            for x in prekazky:
                                if not checkpoint_reached and postava_rect.right > prekazky[30].left and new_x_ctverec < 8000:  
                                    checkpoint_reached = True  # Uložit dosažení checkpointu
                                    print("Checkpoint dosažen!")  
                                    new_x_ctverec = 5175
                                    new_y_ctverec = 0
                                    cervena_zivot1 = (255, 0, 0)
                                    cervena_zivot2 = (255, 0, 0)
                                    cervena_zivot3 = (255, 0, 0)
                                    if postava_rect.left < prekazky[30].left and new_x_ctverec < 8000:
                                        new_x_ctverec = 5175
                                        new_y_ctverec = 0
                    
                                    
                    elif cervena_zivot3 == (0, 0, 0) and cervena_zivot2 == (255, 0, 0):
                        cervena_zivot2 = (0, 0, 0)
                        cervena_zivot1 = (255, 0, 0)
                        new_y_ctverec = 100
                        new_x_ctverec = 100
                        if len(prekazky) > 30:
                            for x in prekazky:
                                if not checkpoint_reached and postava_rect.right > prekazky[30].left and new_x_ctverec < 8000:  
                                    checkpoint_reached = True  # Uložit dosažení checkpointu
                                    print("Checkpoint dosažen!")  
                                    new_x_ctverec = 5175
                                    new_y_ctverec = 0
                                    cervena_zivot1 = (255, 0, 0)
                                    cervena_zivot2 = (255, 0, 0)
                                    cervena_zivot3 = (255, 0, 0)
                                    if postava_rect.left < prekazky[30].left  and new_x_ctverec < 8000:
                                        new_x_ctverec = 5175
                                        new_y_ctverec = 0
                    else:
                        cervena_zivot1 = (0, 0, 0)
                        new_y_ctverec = 100
                        new_x_ctverec = 100
                        if len(prekazky) > 30:
                            for x in prekazky:
                                if not checkpoint_reached and postava_rect.right > prekazky[30].left and new_x_ctverec < 8000:  
                                    checkpoint_reached = True  # Uložit dosažení checkpointu
                                    print("Checkpoint dosažen!")  
                                    new_x_ctverec = 5175
                                    new_y_ctverec = 0
                                    cervena_zivot1 = (255, 0, 0)
                                    cervena_zivot2 = (255, 0, 0)
                                    cervena_zivot3 = (255, 0, 0)
                                    if postava_rect.left < prekazky[30].left and new_x_ctverec < 8000:
                                        new_x_ctverec = 5175
                                        new_y_ctverec = 0

    # Na konci herního cyklu resetujte stav kolize, pokud není postava v kolizi
    if not je_v_kolizi:
        je_v_kolizi = False


    
    
    
    if 7770 < new_x_ctverec < 7840 and new_x_ctverec >= 394:
        new_x_ctverec = 10000
        new_y_ctverec = 200

    
    
    
    
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
    

    
    boss = pygame.Rect(bossx, bossy, 52, 52)
    bosss = pygame.Rect(bossx - posun_sveta, bossy, 52, 52)
    

    # Vykreslení hitboxů pro ladění
   
    pygame.draw.rect(screen, (0, 0, 0), bosss)  # Zelený rámeček bosse

       # Detekce kolize
    if postava_rect.colliderect(boss):
        print("Kolize s bossem!")
        if cervena_zivot3 == (255, 0, 0):
            cervena_zivot3 = (0, 0, 0)
        elif cervena_zivot3 == (0, 0, 0) and cervena_zivot2 == (255, 0, 0):
            cervena_zivot2 = (0, 0, 0)
            cervena_zivot1 = (255, 0, 0)
        else:
            cervena_zivot1 = (0, 0, 0)


    # Můžeš zde přidat další logiku, např. ubrání života nebo konec hry
    pygame.draw.circle(screen, barva_ocí, (bossx - posun_sveta + 18 , bossy + 17), 8),
    pygame.draw.circle(screen, barva_zornic, (bossx - posun_sveta + 18, bossy + 17), 4),   
    pygame.draw.circle(screen, barva_ocí, (bossx - posun_sveta + 36, bossy + 17), 8),  
    pygame.draw.circle(screen, barva_zornic, (bossx - posun_sveta + 36, bossy + 17), 4),   

    
   
    # Tady si dodělej, co se má stát



    # Zde můžeš přidat další logiku pro vykreslování bosse nebo jiné herní mechaniky

    
    
    
    
    
    pygame.draw.rect(screen, (255, 0, 0), (5100 - posun_sveta, 100, 250, 30)) 
    
    
    pygame.draw.rect(screen, (0, 255, 0), (posledni_prekazka.x - posun_sveta, posledni_prekazka.y, posledni_prekazka.width, posledni_prekazka.height))
    pygame.draw.rect(screen, (0, 255, 0), (posledni_prekazkay.x, posledni_prekazkay.y, posledni_prekazkay.width, posledni_prekazkay.height))
    
    font = pygame.font.Font(None, 50)  # None znamená výchozí font, 36 je velikost písma
    text = "level 1"  # Text, který chcete vykreslit
    text_surface = font.render(text, True, (0, 0, 0))  # Bílý text
    text_rect = text_surface.get_rect(center=(rozliseni_sirka // 2, 50))  # Umístění textu na obrazovku
    screen.blit(text_surface, text_rect)  # Vykreslení textu na obrazovku
        
    
    font = pygame.font.Font(None, 50)  # None znamená výchozí font, 36 je velikost písma
    text = "checkpoint"  # Text, který chcete vykreslit
    text_surface = font.render(text, True, (255, 255, 255))  # Bílý text
    text_rect = text_surface.get_rect(center=(5225 - posun_sveta, 200))  # Umístění textu na obrazovku
    screen.blit(text_surface, text_rect)  # Vykreslení textu na obrazovku
    
    cerna = (0,0,0)
        
    if cervena_zivot1 == (0,0,0) and cervena_zivot2 == (0,0,0) and cervena_zivot3 == (0,0,0):
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 255, 255), rect1, 2)
        pygame.draw.rect(screen, (255, 255, 255), rect2, 2)
        font = pygame.font.Font(None, 36)  # None znamená výchozí font, 36 je velikost písma
        text = "hrát znovu"  # Text, který chcete vykreslit
        text_surface = font.render(text, True, (255, 255, 255))  # Bílý text
        text_rect = text_surface.get_rect(center=(220, 275))  # Umístění textu na obrazovku
        screen.blit(text_surface, text_rect)  # Vykreslení textu na obrazovku
        font = pygame.font.Font(None, 36)  # None znamená výchozí font, 36 je velikost písma
        text = "ukončit hru"  # Text, který chcete vykreslit
        text_surface = font.render(text, True, (255, 255, 255))  # Bílý text
        text_rect = text_surface.get_rect(center=(600, 275))  # Umístění textu na obrazovku
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
    
    if pohyb_bossa and boss_timer is None:
        boss_timer = pygame.time.get_ticks()

    # Vypočítáme uplynulý čas (pouze pokud byl boss_timer nastaven)
    if boss_timer is not None:
        elapsed_time = (pygame.time.get_ticks() - boss_timer) // 1000

        if elapsed_time >= 60:
            print("Uběhlo 30 sekund! Boss se zastaví.")
            pohyb_bossa = False
            boss_timer = None  # Resetujeme časovač
    
    pygame.display.update()
    
    clock.tick(50) 