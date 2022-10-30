import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
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


def draw_cross(number_field):
    top_left_x = 150
    top_left_y = 50
    shift_x = number_field % 3 * 100
    shift_y = number_field // 3 * 100
    pygame.draw.line(screen, RED, (top_left_x + shift_x, top_left_y + shift_y),
                     (top_left_x + 100 + shift_x, top_left_y + 100 + shift_y), 3)
    pygame.draw.line(screen, RED, (top_left_x + shift_x, top_left_y + 100 + shift_y),
                     (top_left_x + 100 + shift_x, top_left_y + shift_y), 3)

def draw_zero():


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                if step:
                    draw_cross(0)
                    step = not step

            if event.key == pygame.K_w:
                if step:
                    pygame.draw.aaline(screen, RED, (200, 50), (130, 100))
                    pygame.draw.aaline(screen, RED, (150, 50), (200, 100))
                else:
                    pygame.draw.circle(screen, BLUE, (300, 100), 50, 3)
    pygame.display.update()
