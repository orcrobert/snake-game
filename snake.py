import pygame
from pygame import color
import time
import random

pygame.init()
height = 550
width = 450
speed = 15
block = 10
dis = pygame.display.set_mode((600, 500))
pygame.display.update()
pygame.display.set_caption('Snake Game')

blue = (0, 0, 255)
black = (0, 0, 0)
red = (255, 0, 0)

clock = pygame.time.Clock()

def showSnake(snake_list):
    for i in snake_list:
        pygame.draw.rect(dis, blue, [i[0], i[1], block, block])


def gameLoop():
    food_x = round(random.randrange(width - block) / 10.0) * 10.0
    food_y = round(random.randrange(height - block) / 10.0) * 10.0
    game_over = False

    x = 300
    y = 250
    x_c = 0
    y_c = 0

    snake_list = []
    length = 1

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_c = -block
                    x_c = 0
                elif event.key == pygame.K_DOWN:
                    y_c = block
                    x_c = 0
                elif event.key == pygame.K_RIGHT:
                    x_c = block
                    y_c = 0
                elif event.key == pygame.K_LEFT:
                    x_c = -block
                    y_c = 0
            
        x += x_c
        y += y_c

        if x < 0 or y < 0 or x >= width or y >= height:
            print("game over")

        dis.fill(black)
        pygame.draw.rect(dis, red, [food_x, food_y, block, block])

        head = []
        head.append(x)
        head.append(y)
        snake_list.append(head)

        if len(snake_list) > length:
            del snake_list[0]

        showSnake(snake_list)
        pygame.display.update()

        if x == food_x and y == food_y:
            length += 1
            food_x = round(random.randrange(0, width - block) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - block) / 10.0) * 10.0
            pygame.draw.rect(dis, red, [food_x, food_y, block, block])

        clock.tick(speed)

    pygame.quit()
    quit()
gameLoop()