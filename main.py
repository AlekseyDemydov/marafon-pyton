import pygame
import numpy as np
from pygame.constants import QUIT

pygame.init()

screen = width, heigth =800, 600

BLACK = 0, 0, 0

random_color=list(np.random.choice(range(255), size=3))

main_surface = pygame.display.set_mode(screen)
ball = pygame.Surface((40, 40))
ball.fill(BLACK)
pygame.draw.circle(ball, random_color, (20, 20), 20)

ball_rect=ball.get_rect()

ball_speed= [1, 1]
is_working = True

while is_working:
    for event in pygame.event.get():
        if event.type == QUIT:
            is_working= False

  
    ball_rect=ball_rect.move(ball_speed)
    if ball_rect.bottom >= heigth or ball_rect.top <= 0:
        ball_speed[1]= -ball_speed[1]
        random_color=list(np.random.choice(range(255), size=3))
        pygame.draw.circle(ball, random_color, (20, 20), 20)
        
    if ball_rect.right >=width or ball_rect.left<=0:
        ball_speed[0]= -ball_speed[0]
        random_color=list(np.random.choice(range(255), size=3))
        pygame.draw.circle(ball, random_color, (20, 20), 20)
       
        
    main_surface.fill((0, 0, 0))
    main_surface.blit(ball, ball_rect)
    # main_surface.fill(155,155,155)
    pygame.display.flip()