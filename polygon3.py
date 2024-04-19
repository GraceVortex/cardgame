import pygame
import sys

class TiltedRectangle:
    def __init__(self, screen, image_path, rect, angle, info_image_path=None, pick_image_path=None, **kwargs):
        self.screen = screen
        self.image = pygame.image.load(image_path)
        self.info_image = pygame.image.load(info_image_path) if info_image_path else None
        self.pick_image = pygame.image.load(pick_image_path) if pick_image_path else None
        self.rect = pygame.Rect(rect)  # Ensure rect is a pygame.Rect object
        self.angle = angle
        self.is_info_visible = False
        self.is_picked = False  # Флаг, показывающий, выбрана ли карта
        # Сохраняем переданные параметры
        self.parameters = kwargs

    def draw(self):
        # Draw the background image
        self.screen.blit(self.screen_bg, (0, 0))
        
        # Rotate and draw the main image
        if self.is_picked and self.pick_image:
            image_to_draw = self.pick_image
        else:
            image_to_draw = self.image
        rotated_image = pygame.transform.rotate(image_to_draw, self.angle)
        rotated_rect = rotated_image.get_rect(center=self.rect.center)
        self.screen.blit(rotated_image, rotated_rect)

        # Optionally draw the info image centered on the screen
        if self.is_info_visible and self.info_image:
            # Center the info image on the screen
            info_rect = self.info_image.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
            self.screen.blit(self.info_image, info_rect)

    def check_click(self, mouse_pos):
        # Check if the click is within the rectangle area
        if self.rect.collidepoint(mouse_pos):
            # Fetch the state of mouse buttons
            left_click, _, right_click = pygame.mouse.get_pressed()
            if left_click:  # Check if left mouse button is pressed
                self.is_picked = not self.is_picked
            elif right_click:  # Check if right mouse button is pressed
                self.is_info_visible = not self.is_info_visible

# Initialize Pygame
pygame.init()
width, height = 1400, 1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tilted Rectangles")

# Load background images
background_image = pygame.image.load("back.png")
backstart_image = pygame.image.load("backstart.png")
screen_bg = pygame.transform.scale(background_image, (width, height))
backstart_bg = pygame.transform.scale(backstart_image, (width, height))

# List of TiltedRectangles with an additional path for info images
rectangles = [
    TiltedRectangle(screen, "enfj.png", (46, 430, 200, 65), 270, "enfj_info.png", pick_image_path="enfj_pick.png", e=90, i=10, n=80, s=20, f=90, t=10, j=60, p=40),
    # Initialize other rectangles similarly with additional parameters
]

# Start button
start_button_rect = pygame.Rect(600, 500, 200, 100)
start_button_color = (0, 0, 0)
start_button_text = pygame.font.SysFont(None, 48).render("Start", True, (255, 255, 255))

# Initial screen state
current_screen = "start"

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if current_screen == "start":
                if start_button_rect.collidepoint(mouse_pos):
                    current_screen = "game"

    screen.fill((255, 255, 255))  # Clear the screen
    if current_screen == "start":
        screen.blit(backstart_bg, (0, 0))
        pygame.draw.rect(screen, start_button_color, start_button_rect)
        screen.blit(start_button_text, (start_button_rect.x + 20, start_button_rect.y + 20))
    elif current_screen == "game":
        screen.blit(screen_bg, (0, 0))
        for rectangle in rectangles:
            rectangle.screen_bg = screen_bg  # Pass background image to the rectangle
            rectangle.draw()  # Draw all the rectangles
            rectangle.check_click(pygame.mouse.get_pos())  # Check for click

    pygame.display.flip()  # Update the display

pygame.quit()
sys.exit()
