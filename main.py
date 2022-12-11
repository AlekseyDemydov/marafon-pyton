import pygame
# import numpy as np
import random
from pygame.constants import QUIT, K_DOWN, K_UP, K_RIGHT, K_LEFT

pygame.init()

FPS=pygame.time.Clock()

screen = width, heigth =800, 600

BLACK = 0, 0, 0
RED = 255, 0, 0
WHITE=255, 255, 255
GREEN=0, 255, 0
YELLOW= 0, 0, 0, 0

# random_color=list(np.random.choice(range(255), size=3))

main_surface = pygame.display.set_mode(screen)
ball = pygame.Surface((40, 40))
ball.fill(BLACK)
ball.set_colorkey(BLACK)
pygame.draw.circle(ball, WHITE, (20, 20), 20)
ball_rect=ball.get_rect()
ball_speed= 5


def create_enemy():
    enemy = pygame.Surface((20, 20))
    enemy_rect=pygame.Rect(width, random.randint(0, heigth), *enemy.get_size())
    enemy.fill(RED)
    enemy_speed=random.randint(2, 5)
    return [enemy, enemy_rect, enemy_speed]

CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 500)

enemies=[]


def create_bonus():
    bonus =pygame.Surface((20, 20))
    bonus_rect=pygame.Rect(random.randint(0, width), 0, *bonus.get_size())
    bonus.fill(GREEN)
    bonus.set_alpha(255)
    bonus.set_colorkey(GREEN)
    pygame.draw.polygon(bonus, WHITE, [(10, 0), (20, 20), (0, 7), (20, 7), (0, 20)],2)
    bonus_speed=random.randint(1, 2)
  
    return [bonus, bonus_rect, bonus_speed]

CREATE_BONUS = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_BONUS, 1500)

bonuses=[]
is_working = True

while is_working:
    FPS.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            is_working= False
        if event.type == CREATE_ENEMY:
            enemies.append(create_enemy())
        if event.type == CREATE_BONUS:
            bonuses.append(create_bonus())
        

    main_surface.fill((0, 0, 0))
    main_surface.blit(ball, ball_rect)
    for enemy in enemies:
         enemy[1]= enemy[1].move(-enemy[2], 0)
         main_surface.blit(enemy[0], enemy[1])

         if enemy[1].left < 0:
            enemies.pop(enemies.index(enemy))

         if ball_rect.colliderect(enemy[1]):
            enemies.pop(enemies.index(enemy))
    
    for bonus in bonuses:
         bonus[1]= bonus[1].move(0, bonus[2])
         main_surface.blit(bonus[0], bonus[1]) 

         if bonus[1].top >=heigth:
            bonuses.pop(bonuses.index(bonus))

         if ball_rect.colliderect(bonus[1]):
            bonuses.pop(bonuses.index(bonus))


    presset_keys =pygame.key.get_pressed()
    if presset_keys[K_DOWN] and not ball_rect.bottom >= heigth:
        ball_rect=ball_rect.move(0, ball_speed)
    if presset_keys[K_UP] and not ball_rect.top <= 0:
        ball_rect=ball_rect.move(0, -ball_speed)
    if presset_keys[K_RIGHT] and not ball_rect.right >= width:
        ball_rect=ball_rect.move(ball_speed, 0)
    if presset_keys[K_LEFT] and not ball_rect.left <= 0:
        ball_rect=ball_rect.move(-ball_speed, 0)

    
  
    # main_surface.fill(155,155,155)
    pygame.display.flip()