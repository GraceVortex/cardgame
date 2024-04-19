import pygame
import random
import math

class Card:
    def __init__(self, mbti_type, image_path):
        self.mbti_type = mbti_type
        self.image = pygame.image.load(image_path)
        self.original_image = self.image  # Store the original image to prevent distortion from multiple rotations
        self.rect = self.image.get_rect()
        self.angle = 0  # Store the angle for each card

    def set_angle(self, angle):
        # Rotate the card so its top points outwards from the center
        self.angle = angle + 90  # Offset by 90 degrees to orient the card correctly
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()

class CardGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1075, 768))  # Set to your new resolution
        pygame.display.set_caption("MBTI Card Game")

        # Load card images and create card objects
        mbti_types = ['ISTJ', 'ISFJ', 'INFJ', 'INTJ',
                      'ISTP', 'ISFP', 'INFP', 'INTP',
                      'ESTP', 'ESFP', 'ENFP', 'ENTP',
                      'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ']
        self.deck = [Card(mbti, f"{mbti.lower()}.png") for mbti in mbti_types]
        self.center_x = self.screen.get_width() // 2
        self.center_y = self.screen.get_height() // 2
        self.radius = 300  # Radius of the circle

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def display_cards_in_circle(self):
        self.screen.fill((0, 0, 0))  # Clear screen
        angle_increment = 360 / len(self.deck)  # Angle between each card

        for index, card in enumerate(self.deck):
            angle = math.radians(angle_increment * index)
            card.set_angle(math.degrees(angle))
            # Place card center at the position on the circumference of the circle
            x = self.center_x + self.radius * math.cos(angle) - (card.rect.width / 2)
            y = self.center_y + self.radius * math.sin(angle) - (card.rect.height / 2)
            card.rect.center = (x, y)
            self.screen.blit(card.image, card.rect)

        pygame.display.flip()

    def run(self):
        running = True
        self.shuffle_deck()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.display_cards_in_circle()
        pygame.quit()

if __name__ == '__main__':
    game = CardGame()
    game.run()
