import pygame
import sys
import random

class TiltedRectangle:
    def __init__(self, screen, image_path, rect, angle, info_image_path=None, pick_image_path=None, **kwargs):
        self.screen = screen
        self.image_path = image_path  # Сохраняем путь к изначальному изображению
        self.image = pygame.image.load(image_path)
        self.info_image_path = info_image_path  # Сохраняем путь к информационному изображению, если оно есть
        self.info_image = pygame.image.load(info_image_path) if info_image_path else None
        self.pick_image_path = pick_image_path  # Сохраняем путь к изображению при выборе, если оно есть
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
    # Ваши определения классов остаются без изменений

    def __init__(self, screen, image_path, rect, angle, **kwargs):
        self.screen = screen
        self.image = pygame.image.load(image_path)
        self.rect = pygame.Rect(rect)
        self.angle = angle
        self.parameters = kwargs
        self.visible = False

    def draw(self):
        if self.visible:
            # Центрирование изображения на экране
            rotated_image = pygame.transform.rotate(self.image, self.angle)
            new_rect = rotated_image.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
            self.screen.blit(rotated_image, new_rect)


def animate_dice():
    global dice_animation_start, current_dice_index, dice_rolling, final_dice_image
    if dice_animation_start is None:
        dice_animation_start = pygame.time.get_ticks()  # Начало анимации
        current_dice_index = 0  # Начать анимацию с первого изображения
    elapsed_time = pygame.time.get_ticks() - dice_animation_start

    if elapsed_time > 4000:  # Продолжительность анимации - 4 секунды
        dice_rolling = False
        dice_animation_start = None
        final_dice_image = random.choice(dice_images)  # Сохранение финального изображения кости
        return final_dice_image
    else:
        frame_duration = 100
        if elapsed_time // frame_duration > current_dice_index:
            current_dice_index = (elapsed_time // frame_duration) % len(dice_images)
        return dice_images[current_dice_index]
    
def get_situation_index(dice_image):
    # Получить индекс изображения кости и возвратить соответствующий индекс Situation
    for index, img in enumerate(dice_images):
        if img == dice_image:
            return index
    return None

pygame.init()
width, height = 1400, 1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tilted Rectangles")

# Инициализация и загрузка изображений
background_image = pygame.image.load("back.png")
backstart_image = pygame.image.load("backstart.png")
screen_bg = pygame.transform.scale(background_image, (width, height))
backstart_bg = pygame.transform.scale(backstart_image, (width, height))
dice_images = [pygame.image.load(f'dice_{i}.png') for i in range(1, 7)]
final_dice_image = None

dice_animation_start = None
current_dice_index = 0
dice_rolling = False
dice_rect = pygame.Rect(width // 2 - 40, height // 2 - 25, 80, 50)

# Инициализация объектов TiltedRectangle и Situation
situations = [Situation(screen, f'situation{i}.png', (700, 500, 200, 200), 0) for i in range(1, 7)]
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
    Situation(screen, "situation1.png", (700, 500, 200, 200), 0, e=70, i=30, n=60, s=40, t=80, f=20, j=60, p=40),
    Situation(screen, "situation2.png", (700, 500, 200, 200), 0, e=70, i=30, n=60, s=40, t=80, f=20, j=60, p=40),
    Situation(screen, "situation1.png", (700, 500, 200, 200), 0, e=70, i=30, n=60, s=40, t=80, f=20, j=60, p=40),
    Situation(screen, "situation2.png", (700, 500, 200, 200), 0, e=70, i=30, n=60, s=40, t=80, f=20, j=60, p=40),
]
start_button_rect = pygame.Rect(600, 500, 200, 100)
start_button_color = (0, 0, 0)
start_button_text = pygame.font.SysFont(None, 48).render("Start", True, (255, 255, 255))
current_screen = "start"
running = True
averages = {}
picked_cards = [rect for rect in rectangles if rect.is_picked]


def calculate_average_parameters(picked_cards):
    if len(picked_cards) < 4:
        return None
    average_params = {}
    for param in ['e', 'i', 'n', 's', 't', 'f', 'j', 'p']:
        average_params[param] = sum(card.parameters[param] for card in picked_cards) / len(picked_cards)
    return average_params

def reset_picked_cards(cards):
    for card in cards:
        if card.is_picked:
            card.is_picked = False
            card.image = pygame.image.load(card.image_path)  # Assuming original image path is stored in image_path attribute

def calculate_total_error(average_params, situation_params):
    param_keys = ['e', 'i', 'n', 's', 't', 'f', 'j', 'p']
    max_error_per_param = 10000  # (100-0)^2
    max_total_error = max_error_per_param * len(param_keys)  # Максимальная общая ошибка
    total_error = 0
    for param in param_keys:
        total_error += (average_params[param] - situation_params[param]) ** 2
    
    precision = 100 * (1 - total_error / max_total_error)
    return max(0, min(100, precision))  # Убедимся, что значение находится в пределах от 0 до 100%

def draw_final_info_panel(screen, situation_params, total_error_1, total_error_2):
    font = pygame.font.SysFont(None, 36)
    # Создание фонового прямоугольника для панели
    panel_rect = pygame.Rect(screen.get_width() // 2 - 150, screen.get_height() // 2 + 150, 300, 250)
    pygame.draw.rect(screen, (0, 0, 255), panel_rect)  # Фон панели синего цвета

    # Текстовые метки для параметров и ошибок
    labels = ['E', 'A', 'M', 'T', 'J', 'F', 'Precision 1', 'Precision 2']
    values = [situation_params.get(param.lower(), 0) for param in ['E', 'A', 'M', 'T', 'J', 'F']]
    values.extend([f"{total_error_1:.2f}%", f"{total_error_2:.2f}%"])

    # Вывод текста параметров и значений
    for i, (label, value) in enumerate(zip(labels, values)):
        text = font.render(f"{label}: {value}", True, (255, 255, 255))  # Текст белого цвета
        screen.blit(text, (panel_rect.x + 10, panel_rect.y + 10 + i * 25))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if current_screen == "start" and start_button_rect.collidepoint(mouse_pos):
                current_screen = "game"
            elif current_screen == "game":
                for rectangle in rectangles:
                    rectangle.check_click(mouse_pos)
                if final_dice_image and dice_rect.collidepoint(mouse_pos):
                    index = get_situation_index(final_dice_image)
                    if index != None:
                        situations[index].visible = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                if not dice_rolling:  # Check that dice animation is not active
                    dice_rolling = True
                    dice_animation_start = None  # Reset the timer for dice animation
            elif event.key == pygame.K_1:
                picked_cards = [rect for rect in rectangles if rect.is_picked]
                averages['1'] = calculate_average_parameters(picked_cards)
                reset_picked_cards(rectangles)
            elif event.key == pygame.K_2:
                picked_cards = [rect for rect in rectangles if rect.is_picked]
                averages['2'] = calculate_average_parameters(picked_cards)
                reset_picked_cards(rectangles)

    if current_screen == "start":
        screen.blit(backstart_bg, (0, 0))
        pygame.draw.rect(screen, start_button_color, start_button_rect)
        screen.blit(start_button_text, (start_button_rect.x + 20, start_button_rect.y + 20))
    elif current_screen == "game":
        screen.blit(screen_bg, (0, 0))  # Draw the game background first
        if dice_rolling:
            dice_image = animate_dice()
            if dice_image:
                final_dice_image = dice_image
                dice_rect = final_dice_image.get_rect(center=(width // 2, height // 2))
                screen.blit(screen_bg, (0, 0))  # Redraw background to clean up previous frames
                screen.blit(final_dice_image, dice_rect)
                pygame.display.update(dice_rect)
        else:
            if final_dice_image:
                dice_rect = final_dice_image.get_rect(center=(width // 2, height // 2))
                screen.blit(final_dice_image, dice_rect)

        for situation in situations:
            situation.draw()  # Draw situation cards first
        
        for rectangle in rectangles:
            rectangle.draw()  # Then draw the tilted rectangles with their info cards possibly overlaying
    if '1' in averages and '2' in averages:
        situation_index = get_situation_index(final_dice_image)
        if situation_index != None:
            situation_params = situations[situation_index].parameters
            total_error_1 = calculate_total_error(averages['1'], situation_params)
            total_error_2 = calculate_total_error(averages['2'], situation_params)

            if total_error_2 < total_error_1:
                end_image = pygame.image.load('end1.png')
            else:
                end_image = pygame.image.load('end2.png')
            screen.blit(end_image, (width // 2 - end_image.get_width() // 2, height // 2 - end_image.get_height() // 2))
            draw_final_info_panel(screen, situations[situation_index].parameters, total_error_1, total_error_2)
    
    pygame.display.flip()

pygame.quit()
sys.exit()