import pygame

class TiltedRectangle:
    def __init__(self, screen, image_path, rect, angle):
        self.screen = screen
        self.image = pygame.image.load(image_path)
        self.rect = rect
        self.angle = angle

    def draw(self):
        # Rotate the image
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        # Get the new rectangle after rotation
        rotated_rect = rotated_image.get_rect(center=self.rect.center)
        # Draw the rotated image on the screen
        self.screen.blit(rotated_image, rotated_rect)

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 1164, 823
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tilted Rectangles")

# Main loop
running = True
rectangles = [
    TiltedRectangle(screen, "enfj.png", (300, 200, 200, 100), 45, "enfj_info.png", e=90, i=10, n=80, s=20, f=90, t=10, j=60, p=40),
    TiltedRectangle(screen, "enfp.png", (300, 200, 200, 100), 45, "enfp_info.png", e=90, i=10, n=80, s=20, f=90, t=10, j=10, p=90),
    TiltedRectangle(screen, "entj.png", (300, 200, 200, 100), 45, "entj_info.png", e=90, i=10, n=80, s=20, f=10, t=90, j=80, p=20),
    TiltedRectangle(screen, "entp.png", (300, 200, 200, 100), 45, "entp_info.png", e=80, i=20, n=70, s=30, f=20, t=80, j=20, p=80),
    TiltedRectangle(screen, "Esfj.png", (300, 200, 200, 100), 45, "Esfj_info.png", e=90, i=10, n=80, s=20, f=90, t=10, j=60, p=40),
    TiltedRectangle(screen, "esfp.png", (300, 200, 200, 100), 45, "esfp_info.png", e=90, i=10, n=80, s=20, f=90, t=10, j=60, p=40),
    TiltedRectangle(screen, "estj.png", (300, 200, 200, 100), 45, "estj_info.png", e=90, i=10, n=80, s=20, f=90, t=10, j=60, p=40),
    TiltedRectangle(screen, "estp.png", (300, 200, 200, 100), 45, "estp_info.png", e=90, i=10, n=80, s=20, f=90, t=10, j=60, p=40),
    TiltedRectangle(screen, "infj.png", (300, 200, 200, 100), 45, "infj_info.png", e=90, i=10, n=80, s=20, f=90, t=10, j=60, p=40),
    TiltedRectangle(screen, "infp.png", (300, 200, 200, 100), 45, "infp_info.png", e=90, i=10, n=80, s=20, f=90, t=10, j=60, p=40),
    TiltedRectangle(screen, "intj.png", (300, 200, 200, 100), 45, "intj_info.png", e=90, i=10, n=80, s=20, f=90, t=10, j=60, p=40),
    TiltedRectangle(screen, "intp.png", (300, 200, 200, 100), 45, "intp_info.png", e=90, i=10, n=80, s=20, f=90, t=10, j=60, p=40),
    TiltedRectangle(screen, "isfj.png", (300, 200, 200, 100), 45, "isfj_info.png", e=90, i=10, n=80, s=20, f=90, t=10, j=60, p=40),
    TiltedRectangle(screen, "isfp.png", (300, 200, 200, 100), 45, "isfp_info.png", e=90, i=10, n=80, s=20, f=90, t=10, j=60, p=40),
    TiltedRectangle(screen, "ISTJ.png", (300, 200, 200, 100), 45, "ISTJ_info.png", e=90, i=10, n=80, s=20, f=90, t=10, j=60, p=40),
    TiltedRectangle(screen, "istp.png", (300, 200, 200, 100), 45, "istp_info.png", e=90, i=10, n=80, s=20, f=90, t=10, j=60, p=40),
    # Add more rectangles here if needed
]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear the screen
    screen.fill((255, 255, 255))
    
    # Draw all the rectangles
    for rectangle in rectangles:
        rectangle.draw()
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
