import pygame

class TiltedRectangle:
    def __init__(self, screen, image_path, rect, angle, pick_image_path=None, **kwargs):
        self.screen = screen
        self.image = pygame.image.load(image_path)
        self.pick_image = pygame.image.load(pick_image_path) if pick_image_path else None
        self.rect = pygame.Rect(rect)  # Ensure rect is a pygame.Rect object
        self.angle = angle
        self.is_picked = False  # Флаг, показывающий, выбрана ли карта
        # Сохраняем переданные параметры
        self.parameters = kwargs

    def draw(self):
        # Rotate and draw the main image or the picked image
        if self.is_picked and self.pick_image:
            image_to_draw = self.pick_image
        else:
            image_to_draw = self.image
        rotated_image = pygame.transform.rotate(image_to_draw, self.angle)
        rotated_rect = rotated_image.get_rect(center=self.rect.center)
        self.screen.blit(rotated_image, rotated_rect)

    def check_click(self, mouse_pos):
        # Check if the click is within the rectangle area
        if self.rect.collidepoint(mouse_pos):
            self.is_picked = not self.is_picked  # Toggle the pick state

# Initialize Pygame
pygame.init()
width, height = 1200, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Player 1 - Choose 4 cards")

# List of TiltedRectangles for the first player's card selection
player1_cards = [
    TiltedRectangle(screen, "enfj.png", (100, 200, 200, 300), 0, "enfj_pick.png", name="ESFJ"),
    TiltedRectangle(screen, "intp.png", (350, 200, 200, 300), 0, "intp_pick.png", name="INTP"),
    TiltedRectangle(screen, "enfp.png", (600, 200, 200, 300), 0, "enfp_pick.png", name="ENFP"),
    TiltedRectangle(screen, "istj.png", (850, 200, 200, 300), 0, "istj_pick.png", name="ISTJ"),
]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left-click
            mouse_pos = event.pos
            for card in player1_cards:
                card.check_click(mouse_pos)

    screen.fill((255, 255, 255))  # Clear the screen
    for card in player1_cards:
        card.draw()  # Draw all the cards
    pygame.display.flip()  # Update the display

pygame.quit()
