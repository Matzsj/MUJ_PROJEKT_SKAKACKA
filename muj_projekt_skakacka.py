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
skace = False

clock = pygame.time.Clock()

# Překážky
VYSKA_ZEM_PREKAZEK = 363
posun_sveta = 0

prekazky = [
    pygame.Rect(800, VYSKA_ZEM_PREKAZEK, 50, 50),
    pygame.Rect(1200, VYSKA_ZEM_PREKAZEK, 50, 50),
    pygame.Rect(1600, VYSKA_ZEM_PREKAZEK, 50, 50)
]

RED = (255, 0, 0)

# Vytvoření okna
screen = pygame.display.set_mode((rozliseni_sirka, rozliseni_vyska))

# Načtení obrázků
try:
    background_image = pygame.image.load('backgroundColorForest.png')
    background_image = pygame.transform.scale(background_image, (rozliseni_sirka, rozliseni_vyska))
except pygame.error as e:
    print(f"Chyba při načítání obrázku: {e}")
    pygame.quit()
    sys.exit()

try:
    postava = pygame.image.load('ufo-removebg-preview.png').convert_alpha()
    postava_rect = postava.get_rect()
    postava_rect.topleft = (100, 75)
except pygame.error as e:
    print(f"Chyba při načítání obrázku postavy: {e}")
    pygame.quit()
    sys.exit()

# Funkce pro detekci kolize
def detekce_kolize(novy_rect, posun_hitboxu=False):
    for prekazka in prekazky:
        if posun_hitboxu:
            upraveny_hitbox_prekazky = prekazka.move(336, 0)  # Posun pouze pro horizontální kolize
        else:
            upraveny_hitbox_prekazky = prekazka  # Při skákání necháme původní hitbox
        
        if novy_rect.colliderect(upraveny_hitbox_prekazky):
            return True
    return False

# Herní smyčka
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Pohyb postavy
    stisknute_klavesy = pygame.key.get_pressed()

    # Horizontální pohyb (s posunutým hitboxem)
    if stisknute_klavesy[pygame.K_a]:  # Pohyb vlevo
        novy_rect = postava_rect.move(-rychlost, 0)
        if not detekce_kolize(novy_rect, posun_hitboxu=True):  # Posunutý hitbox pro detekci
            postava_rect = novy_rect

    if stisknute_klavesy[pygame.K_d]:  # Pohyb vpravo
        novy_rect = postava_rect.move(rychlost, 0)
        if not detekce_kolize(novy_rect, posun_hitboxu=True):  # Posunutý hitbox pro detekci
            postava_rect = novy_rect

    # Skok
    if stisknute_klavesy[pygame.K_SPACE] and not skace:
        y_velocity = vyska_skoku
        skace = True

    # Aplikace gravitace
    y_velocity += gravitace
    novy_rect = postava_rect.move(0, y_velocity)
    # Vertikální kolize (s původním hitboxem překážky)
    if not detekce_kolize(novy_rect, posun_hitboxu=False):
        postava_rect = novy_rect
    else:
        if y_velocity > 0:  # Pokud padáme a narazíme na překážku
            postava_rect.bottom = novy_rect.top
            y_velocity = 0
            skace = False
        elif y_velocity < 0:  # Pokud skáčeme nahoru a narazíme
            postava_rect.top = novy_rect.bottom
            y_velocity = 0

    # Přistání na zemi (zabraňuje propadnutí skrz podlahu)
    if postava_rect.bottom >= 508:
        postava_rect.bottom = 508
        y_velocity = 0
        skace = False

    # Posun kamery tak, aby hráč byl uprostřed obrazovky
    posun_sveta = postava_rect.x - rozliseni_sirka // 2 + postava_rect.width // 2

    # Vykreslení
    screen.blit(background_image, (0, 0))

    # Vykreslení překážek s posunem světa
    for prekazka in prekazky:
        pygame.draw.rect(screen, RED, (prekazka.x - posun_sveta, prekazka.y, prekazka.width, prekazka.height))

    # Vykreslení postavy na střed obrazovky
    screen.blit(postava, (rozliseni_sirka // 2 - postava_rect.width // 2, postava_rect.y))

    pygame.display.update()
    clock.tick(60)
