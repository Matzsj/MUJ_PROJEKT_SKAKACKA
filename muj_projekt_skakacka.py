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
y_ctverec = 363  # Počáteční výška na zemi (363)
rychlost = 5  # Rychlost pohybu

gravitace = 1
y_velocity = 0 
vyska_skoku = -15  # Záporná hodnota pro skok

skace = False

screen = pygame.display.set_mode((rozliseni_sirka, rozliseni_vyska))

# Načtení pozadí
try:
    background_image = pygame.image.load('backgroundColorForest.png')
    background_image = pygame.transform.scale(background_image, (rozliseni_sirka, rozliseni_vyska))
except pygame.error as e:
    print(f"Chyba při načítání obrázku: {e}")
    pygame.quit()
    sys.exit()

clock = pygame.time.Clock()  # Inicializace hodin

# Hlavní smyčka hry
while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()   

    # Kontrola stisknutých kláves pro pohyb čtverce
    klavesy = pygame.key.get_pressed()
    
    if klavesy[pygame.K_a]:  # A pro pohyb vlevo
        x_ctverec -= rychlost
    if klavesy[pygame.K_d]:  # D pro pohyb vpravo
        x_ctverec += rychlost
        
    # Skok
    if klavesy[pygame.K_SPACE] and not skace:  # Pokud je stisknuto mezerní a ne skáče
        y_velocity = vyska_skoku  # Nastavíme počáteční rychlost skoku
        skace = True  # Nastavíme skáče na True

    # Gravitace a pohyb
    y_ctverec += y_velocity  # Přidáme rychlost y k pozici
    y_velocity += gravitace  # Zvyšujeme rychlost y o gravitaci

    # Ověření, zda je čtverec na zemi
    if y_ctverec >= 363:  # Pokud je čtverec na zemi
        y_ctverec = 363  # Resetujeme pozici na zem
        y_velocity = 0  # Resetujeme rychlost na 0
        skace = False  # Umožníme další skok

    # Vyplnění obrazovky pozadím
    screen.blit(background_image, (0, 0))

    # Kreslení čtverce
    pygame.draw.rect(screen, barva_ctverce, (x_ctverec, y_ctverec, 50, 50))

    # Kreslení očí
    pygame.draw.circle(screen, barva_ocí, (x_ctverec + 15, y_ctverec + 15), 10)  # Levé oko
    pygame.draw.circle(screen, barva_zornic, (x_ctverec + 15, y_ctverec + 15), 5)   # Zornice

    pygame.draw.circle(screen, barva_ocí, (x_ctverec + 35, y_ctverec + 15), 10)  # Pravé oko
    pygame.draw.circle(screen, barva_zornic, (x_ctverec + 35, y_ctverec + 15), 5)   # Zornice

    pygame.display.update()
    
    clock.tick(60)  # Nastavujeme FPS na 60
