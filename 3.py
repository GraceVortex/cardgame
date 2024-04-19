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
    TiltedRectangle(screen, "enfj.png", pygame.Rect(300, 200, 150, 210), 270),
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
