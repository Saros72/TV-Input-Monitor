import pygame
import sys

pygame.init()
pygame.key.stop_text_input()

# --- BARVY ---
BG = (18, 18, 18)
GREEN = (46, 204, 113)
RED = (231, 76, 60)
WHITE = (255, 255, 255)
GRAY = (160, 160, 160)

# --- OKNO (LANDSCAPE) ---
info = pygame.display.Info()
sw, sh = info.current_w, info.current_h

if sh > sw:
    sw, sh = sh, sw

screen = pygame.display.set_mode((sw, sh))

# --- FONTY (větší URL, menší button) ---
font_title = pygame.font.SysFont("sans-serif", int(sh * 0.08), bold=True)
font_url = pygame.font.SysFont("monospace", int(sh * 0.06), bold=True)
font_btn = pygame.font.SysFont("sans-serif", int(sh * 0.035), bold=True)

clock = pygame.time.Clock()

running = True
server_running = False

SERVER_URL = "http://127.0.0.1:9777"

while running:
    screen.fill(BG)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_RETURN, pygame.K_SPACE]:
                server_running = not server_running

    # ===== TITULEK =====
    title_text = "SERVER RUNNING" if server_running else "SERVER STOPPED"
    title_color = GREEN if server_running else RED

    title = font_title.render(title_text, True, title_color)
    screen.blit(title, (sw//2 - title.get_width()//2, int(sh * 0.15)))

    # ===== URL (větší a výraznější) =====
    url_color = WHITE if server_running else GRAY
    url_text = font_url.render(SERVER_URL, True, url_color)

    screen.blit(url_text, (sw//2 - url_text.get_width()//2, int(sh * 0.38)))

    # ===== MALÉ TLAČÍTKO =====
    bw, bh = int(sw * 0.22), int(sh * 0.10)   # menší než předtím

    rect = pygame.Rect(
        sw // 2 - bw // 2,
        int(sh * 0.70),
        bw,
        bh
    )

    btn_color = GREEN if not server_running else RED
    label = "START" if not server_running else "STOP"

    pygame.draw.rect(screen, btn_color, rect, border_radius=18)
    pygame.draw.rect(screen, GRAY, rect, width=2, border_radius=18)

    txt = font_btn.render(label, True, WHITE)
    screen.blit(
        txt,
        (
            rect.centerx - txt.get_width() // 2,
            rect.centery - txt.get_height() // 2
        )
    )

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()