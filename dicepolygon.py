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
    TiltedRectangle(screen, "enfj.png", (46, 430, 200, 65), 270, "enfj_info.png", "enfj_pick.png", e=90, i=10, n=80, s=20, f=90, t=10, j=60, p=40),
    TiltedRectangle(screen, "enfp.png", (46, 560, 200, 65), 270, "enfp_info.png", "enfp_pick.png", e=90, i=10, n=80, s=20, f=90, t=10, j=60, p=40),
    TiltedRectangle(screen, "entj.png", (535, 865, 200, 65), 0, "entj_info.png", "entj_pick.png",e=90, i=10, n=80, s=20, f=10, t=90, j=80, p=20),
    TiltedRectangle(screen, "entp.png", (530, 80, 200, 65), 0, "entp_info.png", "entp_pick.png",e=80, i=20, n=70, s=30, f=20, t=80, j=20, p=80),
    TiltedRectangle(screen, "Esfj.png", (1053, 725, 200, 65), 49, "esfj_info.png", "esfj_pick.png", e=90, i=10, n=80, s=20, f=90, t=10, j=60, p=40),
    TiltedRectangle(screen, "esfp.png", (280, 805, 200, 65), 311, "esfp_info.png","esfp_pick.png", e=90, i=10, n=80, s=20, f=90, t=10, j=60, p=40),
    TiltedRectangle(screen, "estj.png", (928, 805, 200, 65), 49, "estj_info.png","estj_pick.png", e=90, i=10, n=80, s=20, f=90, t=10, j=60, p=40),
    TiltedRectangle(screen, "estp.png", (928, 115, 200, 65), 130, "estp_info.png","estp_pick.png", e=90, i=10, n=80, s=20, f=90, t=10, j=60, p=40),
    TiltedRectangle(screen, "infj.png", (1150, 560, 200, 65), 90, "infj_info.png","infj_pick.png", e=90, i=10, n=80, s=20, f=90, t=10, j=60, p=40),
    TiltedRectangle(screen, "infp.png", (1150, 430, 200, 65), 90, "infp_info.png", "infp_pick.png",e=90, i=10, n=80, s=20, f=90, t=10, j=60, p=40),
    TiltedRectangle(screen, "intj.png", (665, 80, 200, 65), 0, "intj_info.png","intj_pick.png", e=90, i=10, n=80, s=20, f=90, t=10, j=60, p=40),
    TiltedRectangle(screen, "intp.png", (695, 865, 200, 65), 0, "intp_info.png","intp_pick.png", e=90, i=10, n=80, s=20, f=90, t=10, j=60, p=40),
    TiltedRectangle(screen, "isfj.png", (280, 115, 200, 65), 228, "isfj_info.png","isfj_pick.png", e=90, i=10, n=80, s=20, f=90, t=10, j=60, p=40),
    TiltedRectangle(screen, "isfp.png", (1045, 205, 200, 65), 130, "isfp_info.png","isfp_pick.png", e=90, i=10, n=80, s=20, f=90, t=10, j=60, p=40),
    TiltedRectangle(screen, "ISTJ.png", (155, 195, 200, 65), 228, "istj_info.png", "istj_pick.png",e=90, i=10, n=80, s=20, f=90, t=10, j=60, p=40),
    TiltedRectangle(screen, "istp.png", (155, 725, 200, 65), 311, "istp_info.png", "istp_pick.png",e=90, i=10, n=80, s=20, f=90, t=10, j=60, p=40),
]

situations = [
    Situation(screen, "situation1.png", (700, 500, 200, 200), 0, e=70, i=30, n=60, s=40, t=80, f=20, j=60, p=40),
    Situation(screen, "situation2.png", (700, 500, 200, 200), 0, e=60, i=40, n=50, s=50, t=60, f=70, j=40, p=60),
    Situation(screen, "situation3.png", (700, 500, 200, 200), 0, e=70, i=30, n=60, s=40, t=80, f=20, j=60, p=40),
    Situation(screen, "situation4.png", (700, 500, 200, 200), 0, e=70, i=30, n=60, s=40, t=80, f=20, j=60, p=40),
    Situation(screen, "situation5.png", (700, 500, 200, 200), 0, e=70, i=30, n=60, s=40, t=80, f=20, j=60, p=40),
    Situation(screen, "situation6.png", (700, 500, 200, 200), 0, e=70, i=30, n=60, s=40, t=80, f=20, j=60, p=40),
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


