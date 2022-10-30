import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400), pygame.RESIZABLE)
pygame.display.set_caption('Cross-zero')
pygame.display.set_icon(pygame.image.load('picture.webp'))
RED = 255, 0, 0
WHITE = 255, 255, 255
BLUE = 0, 0, 255
screen.fill(WHITE)
step = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                if step:
                    pygame.draw.aaline(screen, RED, (200, 50), (130, 100))
                    pygame.draw.aaline(screen, RED, (150, 50), (200, 100))
                    step = not step
            if event.key == pygame.K_w:
                if step:
                    pygame.draw.aaline(screen, RED, (200, 50), (130, 100))
                    pygame.draw.aaline(screen, RED, (150, 50), (200, 100))
                else:
                    pygame.draw.circle(screen, BLUE, (280, 70), 30, 10)
    pygame.display.update()
