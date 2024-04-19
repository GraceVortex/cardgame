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
width, height = 1200, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tilted Rectangles")

# Main loop
running = True
rectangles = [
    TiltedRectangle(screen, "enfj.png", pygame.Rect(300, 200, 200, 100), 45),
    TiltedRectangle(screen, "enfp.png", pygame.Rect(300, 200, 200, 100), 45),
    TiltedRectangle(screen, "entj.png", pygame.Rect(300, 200, 200, 100), 45),
    TiltedRectangle(screen, "entp.png", pygame.Rect(300, 200, 200, 100), 45),
    TiltedRectangle(screen, "Esfj.png", pygame.Rect(300, 200, 200, 100), 45),
    TiltedRectangle(screen, "esfp.png", pygame.Rect(300, 200, 200, 100), 45),
    TiltedRectangle(screen, "estj.png", pygame.Rect(300, 200, 200, 100), 45),
    TiltedRectangle(screen, "estp.png", pygame.Rect(300, 200, 200, 100), 45),
    TiltedRectangle(screen, "infj.png", pygame.Rect(300, 200, 200, 100), 45),
    TiltedRectangle(screen, "infp.png", pygame.Rect(300, 200, 200, 100), 45),
    TiltedRectangle(screen, "intj.png", pygame.Rect(300, 200, 200, 100), 45),
    TiltedRectangle(screen, "intp.png", pygame.Rect(300, 200, 200, 100), 45),
    TiltedRectangle(screen, "isfj.png", pygame.Rect(300, 200, 200, 100), 45),
    TiltedRectangle(screen, "isfp.png", pygame.Rect(300, 200, 200, 100), 45),
    TiltedRectangle(screen, "ISTJ.png", pygame.Rect(300, 200, 200, 100), 45),
    TiltedRectangle(screen, "istp.png", pygame.Rect(300, 200, 200, 100), 45),
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
