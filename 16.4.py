#coding=utf-8
import pygame,sys
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
my_ball = pygame.image.load("beach_ball.png")#把秋栽入到my_ball
x = 50
y = 50
x_speed = 10
y_speed = 10

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT : sys.exit()

    pygame.time.delay(20)
    pygame.draw.rect(screen,[255,255,255],[x,y,90,90],0)
    x = x + x_speed
    y = y + y_speed
    if x > screen.get_width() - 90 or x < 0 :   #判断当球体达到两侧的边界时
        x_speed = - x_speed #移动速度改为负则形成反弹效果
    if y > screen.get_width() - 90 or y < 0 :   #判断当球体达到两侧的边界时
        y_speed = - y_speed #移动速度改为负则形成反弹效果
    screen.blit(my_ball,[x,y])
    pygame.display.flip()





    '''screen.blit(my_ball,[x,y])#创建一个秋位置在50,50
    pygame.display.flip()
    for looper in range(1, 200):
        pygame.time.delay(20)
        pygame.draw.rect(screen,[255,255,255],[x,y,90,90],0)
        x = x + 5
        screen.blit(my_ball,[x,y])
        pygame.display.flip()
    pygame.time.delay(2000)#延迟2000ms
    screen.blit(my_ball,[150,50])
    pygame.draw.rect(screen,[255,255,255],[50,50,90,90],0)  #擦掉第一个球
    pygame.display.flip()
    '''
