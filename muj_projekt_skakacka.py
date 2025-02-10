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

# Překážky
VYSKA_ZEM_PREKAZEK = 363

posun_sveta = 0

skok = 0

prekazky = [
    pygame.Rect(20, VYSKA_ZEM_PREKAZEK, 50, 50), 
    pygame.Rect(800, VYSKA_ZEM_PREKAZEK, 50, 50),
    pygame.Rect(1200, VYSKA_ZEM_PREKAZEK, 50, 50),
    pygame.Rect(1600, VYSKA_ZEM_PREKAZEK, 50, 50)
]

RED = (255, 0, 0)

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
    postava_rect = postava.get_rect(topleft=(pozice_x_hrace, pozice_y_hrace))
except pygame.error as e:
    print(f"Chyba při načítání obrázku postavy: {e}")
    pygame.quit()
    sys.exit()

# Funkce pro detekci kolize
def detekce_kolize(novy_posun_světa):
    # Pro každou překážku
    for prekazka in prekazky:
        nova_pozice_postavy = postava_rect.move(novy_posun_světa, 0)  # Pohyb pouze horizontálně
        if nova_pozice_postavy.colliderect(prekazka):  # Kolize s překážkou
            return True  # Kolize, hráč se nemůže pohnout
    return False  # Není kolize

# Herní smyčka
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()

    # Pohyb světa kolem hráče
    stisknute_klavesy = pygame.key.get_pressed()
    nova_posun_x = 0  # Počáteční hodnota posunu

    if stisknute_klavesy[pygame.K_a]:  # Pohyb vlevo
        nova_posun_x = -rychlost  # Posun doprava (posouváme okolí doleva)
    if stisknute_klavesy[pygame.K_d]:  # Pohyb vpravo
        nova_posun_x = rychlost  # Posun doleva (posouváme okolí doprava)

    # Zkontroluj, zda by pohyb způsobil kolizi s překážkami
    if not detekce_kolize(nova_posun_x):  # Pokud není kolize, posuň svět
        posun_sveta += nova_posun_x  # Posuneme svět (obrázky se posunou)
        postava_rect.x += nova_posun_x  # Posuneme hráče (vypadá to, že se pohybuje)

    # Skákání a gravitace
    if stisknute_klavesy[pygame.K_SPACE] and not skace:
        y_velocity = vyska_skoku
        skace = True

    # Aplikace gravitace
    pozice_y_hrace += y_velocity
    y_velocity += gravitace

    # Přistání na zemi
    if pozice_y_hrace >= VYSKA_ZEM_PREKAZEK:
        pozice_y_hrace = VYSKA_ZEM_PREKAZEK
        y_velocity = 0
        skace = False

    # Vykreslení pozadí
    screen.blit(background_image, (0, 0))

    # Vykreslení překážek
    for prekazka in prekazky:
        pygame.draw.rect(screen, RED, (prekazka.x - posun_sveta, prekazka.y, prekazka.width, prekazka.height))

    # Vykreslení postavy
    screen.blit(postava, postava_rect.topleft)

    pygame.display.update()
    clock.tick(60)
