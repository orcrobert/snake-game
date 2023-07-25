import pygame
from pygame import color
import time
import random

pygame.init()
height = 600
width = 600
speed = 15
block = 10

font = pygame.font.SysFont("consolas", 18)
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

def showScore(length):
    val = font.render("Score: " + str(length - 1), True, blue)
    dis.blit(val, [0, 0])

def showOverMessage():
    message = font.render("Loser! Press Q to quit or C to continue.", True, blue)
    dis.blit(message, [100, 150])

def getFoodCoordinatesX():
    cx = round(random.randrange(0, width - block) / 10.0) * 10.0
    while cx < 0 and cx >= width:
        getFoodCoordinatesX()
    print(str(cx) + " ")
    return cx

def getFoodCoordinatesY():
    cy = round(random.randrange(0, height - block) / 10.0) * 10.0
    while cy < 0 and cy >= height:
        getFoodCoordinatesY()
    print(str(cy) + "\n")
    return cy

def gameLoop():
    food_x = getFoodCoordinatesX()
    food_y = getFoodCoordinatesY()
    game_over = False
    close = False

    x = width / 2
    y = height / 2
    x_c = 0
    y_c = 0

    snake_list = []
    length = 1

    while not game_over:
        while close == True:
            dis.fill(black)
            showOverMessage()
            showScore(length)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        close = False
                    elif event.key == pygame.K_c:
                        gameLoop()

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
            close = True

        dis.fill(black)
        pygame.draw.rect(dis, red, [food_x, food_y, block, block])

        head = []
        head.append(x)
        head.append(y)
        snake_list.append(head)

        if len(snake_list) > length:
            del snake_list[0]
        
        for i in snake_list[:-1]:
            if i == head:
                close = True

        showSnake(snake_list)
        showScore(length)

        if x == food_x and y == food_y:
            length += 1
            food_x = getFoodCoordinatesX()
            food_y = getFoodCoordinatesY()
            pygame.draw.rect(dis, red, [food_x, food_y, block, block])

        pygame.display.update()
        clock.tick(speed)

    pygame.quit()
    quit()
gameLoop()