import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400), pygame.FULLSCREEN)
pygame.display.set_caption('Cross-zero')
pygame.display.set_icon(pygame.image.load('picture.webp'))
RED = 255, 0, 0
WHITE = 255, 255, 255
BLUE = 0, 0, 255
BLACK = 0, 0, 0
screen.fill(WHITE)
step = True
pygame.draw.rect(screen, BLACK, (150, 50, 300, 300), 3)
pygame.draw.rect(screen, BLACK, (250, 50, 100, 300), 3)
pygame.draw.rect(screen, BLACK, (150, 150, 300, 100), 3)
FPS = 60
clock = pygame.time.Clock()
One_in_One = []
a = ['q']


# [0]


# Рисуем крестик по номеру на схеме
# 012
# 345
# 678
def draw_cross(number_field):
    top_left_x = 150
    top_left_y = 50
    shift_x = number_field % 3 * 100
    shift_y = number_field // 3 * 100
    pygame.draw.line(screen, RED, (top_left_x + shift_x, top_left_y + shift_y),
                     (top_left_x + 100 + shift_x, top_left_y + 100 + shift_y), 3)
    pygame.draw.line(screen, RED, (top_left_x + shift_x, top_left_y + 100 + shift_y),
                     (top_left_x + 100 + shift_x, top_left_y + shift_y), 3)


def draw_zero(number_area):
    if number_area == 0 or number_area == 1 or number_area == 2:
        pygame.draw.circle(screen, BLUE, (200 + (100 * number_area), 100), 50, 3)
    if number_area == 3 or number_area == 4 or number_area == 5:
        pygame.draw.circle(screen, BLUE, (200 + (100 * (number_area - 3)), 200), 50, 3)
    if number_area == 6 or number_area == 7 or number_area == 8:
        pygame.draw.circle(screen, BLUE, (200 + (100 * (number_area - 6)), 300), 50, 3)


while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                if not (0 in One_in_One) or not (1 in One_in_One):
                    if step:
                        draw_cross(0)
                        step = not step
                        One_in_One.append(0)
                    else:
                        draw_zero(0)
                        step = not step
                        One_in_One.append(1)
                else:
                    ...
            if event.key == pygame.K_w:
                if not (2 in One_in_One) or not (3 in One_in_One):
                    if step:
                        draw_cross(1)
                        step = not step
                        One_in_One.append(2)
                    else:
                        draw_zero(1)
                        step = not step
                        One_in_One.append(3)
                else:
                    ...
            if event.key == pygame.K_e:
                if not (4 in One_in_One) or not (5 in One_in_One):
                    if step:
                        draw_cross(2)
                        step = not step
                        One_in_One.append(4)
                    else:
                        draw_zero(2)
                        step = not step
                        One_in_One.append(5)
                else:
                    ...
            if event.key == pygame.K_a:
                if not (6 in One_in_One) or not (7 in One_in_One):
                    if step:
                        draw_cross(3)
                        step = not step
                        One_in_One.append(6)
                    else:
                        draw_zero(3)
                        step = not step
                        One_in_One.append(7)
                else:
                    ...
            if event.key == pygame.K_s:
                if not (8 in One_in_One) or not (9 in One_in_One):
                    if step:
                        draw_cross(4)
                        step = not step
                        One_in_One.append(8)
                    else:
                        draw_zero(4)
                        step = not step
                        One_in_One.append(9)
                else:
                    ...
            if event.key == pygame.K_d:
                if not (10 in One_in_One) or not (11 in One_in_One):
                    if step:
                        draw_cross(5)
                        step = not step
                        One_in_One.append(10)
                    else:
                        draw_zero(5)
                        step = not step
                        One_in_One.append(11)
                else:
                    ...
            if event.key == pygame.K_z:
                if not (12 in One_in_One) or not (13 in One_in_One):
                    if step:
                        draw_cross(6)
                        step = not step
                        One_in_One.append(12)
                    else:
                        draw_zero(6)
                        step = not step
                        One_in_One.append(13)
            else:
                ...
            if event.key == pygame.K_x:
                if not (14 in One_in_One) or not (15 in One_in_One):
                    if step:
                        draw_cross(7)
                        step = not step
                        One_in_One.append(14)
                    else:
                        draw_zero(7)
                        step = not step
                        One_in_One.append(15)
                else:
                    ...
            if event.key == pygame.K_c:
                if not (16 in One_in_One) or not (17 in One_in_One):
                    if step:
                        draw_cross(8)
                        step = not step
                        One_in_One.append(16)
                    else:
                        draw_zero(8)
                        step = not step
                        One_in_One.append(17)
                else:
                    ...

    pygame.display.update()
