#coding=utf-8
import pygame,sys,math #math是导入数学函数

pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
plotPoints = []
for x in range(0 , 640):
    y = int (math.sin(x/640.0 * 4 * math.pi) * 200 + 240 )  #计算每一个点的Y坐标
    plotPoints.append([x,y]) #将每一个点添加到列表（数组）
pygame.draw.lines(screen,[0,0,0],False,plotPoints,1)#用函数lines画出整条曲线 参数分别是 画线的表面（载体），颜色，是否要将最后一个点和第一个点闭合，要链接点的列表（数组），线宽
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()