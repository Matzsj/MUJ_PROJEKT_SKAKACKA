import sys
import pygame
import subprocess

# Inicializace Pygame
pygame.mixer.init()
pygame.init()

# Rozměry okna
rozliseni_vyska = 600
rozliseni_sirka = 800

# Obdélníky pro tlačítka
rect1 = pygame.Rect(400, 330, 250, 50)
rect2 = pygame.Rect(400, 430, 250, 50)

# Načtení hudby
pygame.mixer.music.load("game-music-loop-7-145285.mp3")
pygame.mixer.music.play(-1)  # -1 znamená opakování do nekonečna

# Vytvoření okna
screen = pygame.display.set_mode((rozliseni_sirka, rozliseni_vyska))

# Načtení pozadí
try:
    background_image = pygame.image.load('hl.menu.png').convert()
    background_image = pygame.transform.scale(background_image, (rozliseni_sirka, rozliseni_vyska))
except pygame.error as e:
    print(f"Chyba při načítání obrázku: {e}")
    pygame.quit()
    sys.exit()

# Inicializace hodin
clock = pygame.time.Clock()

# Fonty
font_title = pygame.font.SysFont("Cambria", 80)
font_button = pygame.font.Font(None, 45)

# Vykreslení názvu hry
text_title = "Hazard Rush"
text_surface_title = font_title.render(text_title, True, (255,255,255))
text_rect_title = text_surface_title.get_rect(center=(rozliseni_sirka // 2, 75))  # Umístění na střed

while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()

        if udalost.type == pygame.MOUSEBUTTONDOWN:    
            if rect2.collidepoint(udalost.pos):
                pygame.quit()
                sys.exit()
            if rect1.collidepoint(udalost.pos):
                pygame.quit()
                subprocess.run(["python", "muj_projekt_skakacka.py"])
                sys.exit()

    # Kreslení
    screen.blit(background_image, (0, 0))
    
    # Kreslení tlačítek
    pygame.draw.rect(screen, (0, 0, 0), rect1, border_radius=20)
    pygame.draw.rect(screen, (0, 0, 0), rect2, border_radius=20)

    # Vykreslení textu tlačítek
    text_buttons = ['HRÁT', 'UKONČIT HRU']
    for i, text in enumerate(text_buttons):
        text_surface = font_button.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(523, 357 + (i * 100)))  # Posun podle indexu
        screen.blit(text_surface, text_rect)  # Vykreslení textu na obrazovku

    # Vykreslení názvu hry
    screen.blit(text_surface_title, text_rect_title)

    pygame.display.update()
    
    # Omezování snímkové frekvence
    clock.tick(50)
