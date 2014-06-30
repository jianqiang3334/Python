#coding=utf-8

import pygame,sys

pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
my_ball = pygame.image.load("beach_ball.png")

x = 50
y = 50
x_speed = 5
y_speed = 10
while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.time.delay(20)
        pygame.draw.rect(screen,[255,255,255,],[x,y,90,90],0)
        x = x + x_speed
        if x > screen.get_width():  #当x值到达窗口临界点
            x = 0   #x归为为0重新计算
        screen.blit(my_ball,[x,y])
        pygame.display.flip()
