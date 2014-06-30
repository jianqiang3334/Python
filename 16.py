#coding=utf-8

import pygame,sys

pygame.init()
screen = pygame.display.set_mode([640,480]) #创建一个大小为640*480的窗口
screen.fill([255,255,255])#填充背景为白色
#pygame.draw.circle(screen,[255,0,0],[100,100],30,0)#画出一个圆形 三个参数为 颜色 位置 半径 还有一个是线宽
pygame.draw.rect(screen,[255,0,0],[250,150,300,200],2) #画出一个矩形参数为 颜色 位置(位置(左 高)  大小(高 宽)
pygame.display.flip() #反转一次动画
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


#from pygame.color import THECOLORS 栽入pygame自带的颜色库 用英文代替颜色名
#pygame.draw.circle(screen, THECOLORS["red"],[100,100],30,0) #使用英文名的写法