#coding=utf-8
import pygame,sys
from pygame.locals import *

class MyBallClass(pygame.sprite.Sprite):
    def _init__(self,image_file,speed,location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left , self.rect.top = location
        self.speed = speed

    def move(self):
        self.rect = self.rect.move(self.speed)
        #在窗口两边反弹
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = - self.speed[0]
        #在窗口顶部反弹
        if self.rect.top <= 0 :
            self.speed[1] = - self.speed[1]

class MyPaddleClass(pygame.sprite.Sprite):
    def __init__(self,location):
        pygame.sprite.Sprite.__init__(self)
        image_surface = pygame.surface.Surface([100,200])
        image_surface.fill([0,0,0])
        self.image = image_surface.convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

pygame.init()
screen = pygame.display.set_mode([640,480])
clock = pygame.time.Clock()
ball_speed = [10,5]
myBall = MyBallClass('wackyball.bmp',ball_speed,[50,50])
ballGroup = pygame.sprite.Group(myBall)
paddle = MyPaddleClass([270,400])

while 1 :
    clock.tick(30)
    screen.fill([255,255,255])
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            paddle.rect.centerx = event.pos[0]

    if pygame.sprite.spritecollide(paddle,ballGroup,False):
        myBall.speed[1] = - myBall.speed[1]
    myBall.move()
    screen.blit(myBall,image,myBall,rect)
    screen.blit(paddle,image,paddle,rect)
    pygame.display.flip()
