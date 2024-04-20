import pygame
import sys

class TiltedRectangle:
    def __init__(self, screen, image_path, rect, angle, info_image_path=None, pick_image_path=None, **kwargs):
        self.screen = screen
        self.image = pygame.image.load(image_path)
        self.info_image = pygame.image.load(info_image_path) if info_image_path else None
        self.pick_image = pygame.image.load(pick_image_path) if pick_image_path else None
        self.rect = pygame.Rect(rect)
        self.angle = angle
        self.is_info_visible = False
        self.is_picked = False
        self.parameters = kwargs

    def draw(self):
        image_to_draw = self.pick_image if self.is_picked and self.pick_image else self.image
        rotated_image = pygame.transform.rotate(image_to_draw, self.angle)
        rotated_rect = rotated_image.get_rect(center=self.rect.center)
        self.screen.blit(rotated_image, rotated_rect)
        if self.is_info_visible and self.info_image:
            info_rect = self.info_image.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
            self.screen.blit(self.info_image, info_rect)

    def check_click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            left_click, _, right_click = pygame.mouse.get_pressed()
            if left_click:
                self.is_picked = not self.is_picked
            elif right_click:
                self.is_info_visible = not self.is_info_visible

class Situation:
    def __init__(self, screen, image_path, rect, angle, **kwargs):
        self.screen = screen
        self.image = pygame.image.load(image_path)
        self.rect = pygame.Rect(rect)
        self.angle = angle
        self.parameters = kwargs

    def draw(self):
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        rotated_rect = rotated_image.get_rect(center=self.rect.center)
        self.screen.blit(rotated_image, rotated_rect)

pygame.init()
width, height = 1400, 1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tilted Rectangles")
background_image = pygame.image.load("back.png")
backstart_image = pygame.image.load("backstart.png")
screen_bg = pygame.transform.scale(background_image, (width, height))
backstart_bg = pygame.transform.scale(backstart_image, (width, height))

rectangles = [
    TiltedRectangle(screen, "enfj.png", (46, 430, 200, 65), 270, "enfj_info.png", e=90, i=10, n=80, s=20, f=90, t=10, j=60, p=40),
    TiltedRectangle(screen, "enfp.png", (100, 200, 200, 100), 90, "enfp_info.png", e=90, i=10, n=80, s=20, f=90, t=10, j=10, p=90),
    TiltedRectangle(screen, "entj.png", (300, 200, 200, 100), 45, "entj_info.png", e=90, i=10, n=80, s=20, f=10, t=90, j=80, p=20),
    TiltedRectangle(screen, "entp.png", (300, 200, 200, 100), 45, "entp_info.png", e=80, i=20, n=70, s=30, f=20, t=80, j=20, p=80),
    TiltedRectangle(screen, "Esfj.png", (300, 200, 200, 100), 45, "esfj_info.png", e=90, i=10, n=80, s=20, f=90, t=10, j=60, p=40),
    TiltedRectangle(screen, "esfp.png", (300, 200, 200, 100), 45, "esfp_info.png", e=90, i=10, n=80, s=20, f=90, t=10, j=60, p=40),
    TiltedRectangle(screen, "estj.png", (300, 200, 200, 100), 45, "estj_info.png", e=90, i=10, n=80, s=20, f=90, t=10, j=60, p=40),
    TiltedRectangle(screen, "estp.png", (300, 200, 200, 100), 45, "estp_info.png", e=90, i=10, n=80, s=20, f=90, t=10, j=60, p=40),
    TiltedRectangle(screen, "infj.png", (300, 200, 200, 100), 45, "infj_info.png", e=90, i=10, n=80, s=20, f=90, t=10, j=60, p=40),
    TiltedRectangle(screen, "infp.png", (300, 200, 200, 100), 45, "infp_info.png", e=90, i=10, n=80, s=20, f=90, t=10, j=60, p=40),
    TiltedRectangle(screen, "intj.png", (300, 200, 200, 100), 45, "intj_info.png", e=90, i=10, n=80, s=20, f=90, t=10, j=60, p=40),
    TiltedRectangle(screen, "intp.png", (300, 200, 200, 100), 45, "intp_info.png", e=90, i=10, n=80, s=20, f=90, t=10, j=60, p=40),
    TiltedRectangle(screen, "isfj.png", (300, 200, 200, 100), 45, "isfj_info.png", e=90, i=10, n=80, s=20, f=90, t=10, j=60, p=40),
    TiltedRectangle(screen, "isfp.png", (300, 200, 200, 100), 45, "isfp_info.png", e=90, i=10, n=80, s=20, f=90, t=10, j=60, p=40),
    TiltedRectangle(screen, "ISTJ.png", (300, 200, 200, 100), 45, "istj_info.png", e=90, i=10, n=80, s=20, f=90, t=10, j=60, p=40),
    TiltedRectangle(screen, "istp.png", (300, 200, 200, 100), 45, "istp_info.png", e=90, i=10, n=80, s=20, f=90, t=10, j=60, p=40),
    # Initialize other rectangles similarly with additional parameters
]

situations = [
    Situation(screen, "situation1.png", (100, 100, 200, 200), 0, e=70, i=30, n=60, s=40, t=80, f=20, j=60, p=40),
    Situation(screen, "situation2.png", (400, 100, 200, 200), 0, e=60, i=40, n=50, s=50, t=60, f=70, j=40, p=60)
]

start_button_rect = pygame.Rect(600, 500, 200, 100)
start_button_color = (0, 0, 0)
start_button_text = pygame.font.SysFont(None, 48).render("Start", True, (255, 255, 255))
current_screen = "start"
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if current_screen == "start" and start_button_rect.collidepoint(mouse_pos):
                current_screen = "game"
            elif current_screen == "game":
                for rectangle in rectangles:
                    rectangle.check_click(mouse_pos)  # Move this to mouse button down

    screen.fill((255, 255, 255))
    if current_screen == "start":
        screen.blit(backstart_bg, (0, 0))
        pygame.draw.rect(screen, start_button_color, start_button_rect)
        screen.blit(start_button_text, (start_button_rect.x + 20, start_button_rect.y + 20))
    elif current_screen == "game":
        screen.blit(screen_bg, (0, 0))
        for rectangle in rectangles:
            rectangle.draw()

    pygame.display.flip()

pygame.quit()
sys.exit()
