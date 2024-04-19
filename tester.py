import pygame

class TiltedRectangle:
    def __init__(self, screen, image_path, rect, angle, info_image_path=None, **kwargs):
        self.screen = screen
        self.image = pygame.image.load(image_path)
        self.info_image = pygame.image.load(info_image_path) if info_image_path else None
        self.rect = pygame.Rect(rect)  # Ensure rect is a pygame.Rect object
        self.angle = angle
        self.is_info_visible = False
        # Сохраняем переданные параметры
        self.parameters = kwargs

    def draw(self):
        # Draw the background image
        self.screen.blit(self.screen_bg, (0, 0))
        
        # Rotate and draw the main image
        rotated_image = pygame.transform.rotate(self.image, self.angle)
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
            if self.is_info_visible:
                self.is_info_visible = False  # Hide info rectangle if already visible
            else:
                self.is_info_visible = True  # Toggle the visibility

# Initialize Pygame
pygame.init()
width, height = 1400, 1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tilted Rectangles")

# Load background image
background_image = pygame.image.load("back.png")
screen_bg = pygame.transform.scale(background_image, (width, height))

# List of TiltedRectangles with an additional path for info images
rectangles = [
    TiltedRectangle(screen, "enfj.png", (46, 430, 200, 65), 270, "Group 1.png", e=90, i=10, n=80, s=20, f=90, t=10, j=60, p=40),
    # Initialize other rectangles similarly with additional parameters
]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:  # Right-click
            mouse_pos = event.pos
            for rectangle in rectangles:
                rectangle.check_click(mouse_pos)

    screen.fill((255, 255, 255))  # Clear the screen
    for rectangle in rectangles:
        rectangle.screen_bg = screen_bg  # Pass background image to the rectangle
        rectangle.draw()  # Draw all the rectangles
    pygame.display.flip()  # Update the display

pygame.quit()
